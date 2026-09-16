from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_domains_domain_registrars_archive_create_annotations_error_component import (
        ApiV1DomainsDomainRegistrarsArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_archive_create_api_backoff_minutes_error_component import (
        ApiV1DomainsDomainRegistrarsArchiveCreateApiBackoffMinutesErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_archive_create_api_credential_id_error_component import (
        ApiV1DomainsDomainRegistrarsArchiveCreateApiCredentialIdErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_archive_create_archived_at_error_component import (
        ApiV1DomainsDomainRegistrarsArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_archive_create_archived_by_error_component import (
        ApiV1DomainsDomainRegistrarsArchiveCreateArchivedByErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_archive_create_archived_error_component import (
        ApiV1DomainsDomainRegistrarsArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_archive_create_archived_reason_error_component import (
        ApiV1DomainsDomainRegistrarsArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_archive_create_created_by_component_error_component import (
        ApiV1DomainsDomainRegistrarsArchiveCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_archive_create_created_by_user_error_component import (
        ApiV1DomainsDomainRegistrarsArchiveCreateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_archive_create_criticality_error_component import (
        ApiV1DomainsDomainRegistrarsArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_archive_create_debug_mode_error_component import (
        ApiV1DomainsDomainRegistrarsArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_archive_create_default_renewal_mode_error_component import (
        ApiV1DomainsDomainRegistrarsArchiveCreateDefaultRenewalModeErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_archive_create_display_name_error_component import (
        ApiV1DomainsDomainRegistrarsArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_archive_create_import_contacts_error_component import (
        ApiV1DomainsDomainRegistrarsArchiveCreateImportContactsErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_archive_create_import_domains_error_component import (
        ApiV1DomainsDomainRegistrarsArchiveCreateImportDomainsErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_archive_create_kind_error_component import (
        ApiV1DomainsDomainRegistrarsArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_archive_create_labels_error_component import (
        ApiV1DomainsDomainRegistrarsArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_archive_create_last_rate_limited_at_error_component import (
        ApiV1DomainsDomainRegistrarsArchiveCreateLastRateLimitedAtErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_archive_create_last_reconciliation_duration_seconds_error_component import (
        ApiV1DomainsDomainRegistrarsArchiveCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_archive_create_managed_by_content_type_error_component import (
        ApiV1DomainsDomainRegistrarsArchiveCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_archive_create_managed_by_object_id_error_component import (
        ApiV1DomainsDomainRegistrarsArchiveCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_archive_create_modified_by_user_error_component import (
        ApiV1DomainsDomainRegistrarsArchiveCreateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_archive_create_name_error_component import (
        ApiV1DomainsDomainRegistrarsArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_archive_create_non_field_errors_error_component import (
        ApiV1DomainsDomainRegistrarsArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_archive_create_ote_error_component import (
        ApiV1DomainsDomainRegistrarsArchiveCreateOteErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_archive_create_platform_dns_record_created_error_component import (
        ApiV1DomainsDomainRegistrarsArchiveCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_archive_create_platform_service_error_component import (
        ApiV1DomainsDomainRegistrarsArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_archive_create_provider_error_component import (
        ApiV1DomainsDomainRegistrarsArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_archive_create_provider_id_error_component import (
        ApiV1DomainsDomainRegistrarsArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_archive_create_provider_info_error_component import (
        ApiV1DomainsDomainRegistrarsArchiveCreateProviderInfoErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_archive_create_provider_reference_error_component import (
        ApiV1DomainsDomainRegistrarsArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_archive_create_reconciliation_enabled_error_component import (
        ApiV1DomainsDomainRegistrarsArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_archive_create_sla_availability_error_component import (
        ApiV1DomainsDomainRegistrarsArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_archive_create_sla_target_error_component import (
        ApiV1DomainsDomainRegistrarsArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_archive_create_sla_window_days_error_component import (
        ApiV1DomainsDomainRegistrarsArchiveCreateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_archive_create_slo_availability_error_component import (
        ApiV1DomainsDomainRegistrarsArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_archive_create_slo_target_error_component import (
        ApiV1DomainsDomainRegistrarsArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_archive_create_slo_window_days_error_component import (
        ApiV1DomainsDomainRegistrarsArchiveCreateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_archive_create_target_availability_error_component import (
        ApiV1DomainsDomainRegistrarsArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_archive_create_tolerations_error_component import (
        ApiV1DomainsDomainRegistrarsArchiveCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1DomainsDomainRegistrarsArchiveCreateValidationError")


@_attrs_define
class ApiV1DomainsDomainRegistrarsArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1DomainsDomainRegistrarsArchiveCreateAnnotationsErrorComponent |
            ApiV1DomainsDomainRegistrarsArchiveCreateApiBackoffMinutesErrorComponent |
            ApiV1DomainsDomainRegistrarsArchiveCreateApiCredentialIdErrorComponent |
            ApiV1DomainsDomainRegistrarsArchiveCreateArchivedAtErrorComponent |
            ApiV1DomainsDomainRegistrarsArchiveCreateArchivedByErrorComponent |
            ApiV1DomainsDomainRegistrarsArchiveCreateArchivedErrorComponent |
            ApiV1DomainsDomainRegistrarsArchiveCreateArchivedReasonErrorComponent |
            ApiV1DomainsDomainRegistrarsArchiveCreateCreatedByComponentErrorComponent |
            ApiV1DomainsDomainRegistrarsArchiveCreateCreatedByUserErrorComponent |
            ApiV1DomainsDomainRegistrarsArchiveCreateCriticalityErrorComponent |
            ApiV1DomainsDomainRegistrarsArchiveCreateDebugModeErrorComponent |
            ApiV1DomainsDomainRegistrarsArchiveCreateDefaultRenewalModeErrorComponent |
            ApiV1DomainsDomainRegistrarsArchiveCreateDisplayNameErrorComponent |
            ApiV1DomainsDomainRegistrarsArchiveCreateImportContactsErrorComponent |
            ApiV1DomainsDomainRegistrarsArchiveCreateImportDomainsErrorComponent |
            ApiV1DomainsDomainRegistrarsArchiveCreateKindErrorComponent |
            ApiV1DomainsDomainRegistrarsArchiveCreateLabelsErrorComponent |
            ApiV1DomainsDomainRegistrarsArchiveCreateLastRateLimitedAtErrorComponent |
            ApiV1DomainsDomainRegistrarsArchiveCreateLastReconciliationDurationSecondsErrorComponent |
            ApiV1DomainsDomainRegistrarsArchiveCreateManagedByContentTypeErrorComponent |
            ApiV1DomainsDomainRegistrarsArchiveCreateManagedByObjectIdErrorComponent |
            ApiV1DomainsDomainRegistrarsArchiveCreateModifiedByUserErrorComponent |
            ApiV1DomainsDomainRegistrarsArchiveCreateNameErrorComponent |
            ApiV1DomainsDomainRegistrarsArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1DomainsDomainRegistrarsArchiveCreateOteErrorComponent |
            ApiV1DomainsDomainRegistrarsArchiveCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1DomainsDomainRegistrarsArchiveCreatePlatformServiceErrorComponent |
            ApiV1DomainsDomainRegistrarsArchiveCreateProviderErrorComponent |
            ApiV1DomainsDomainRegistrarsArchiveCreateProviderIdErrorComponent |
            ApiV1DomainsDomainRegistrarsArchiveCreateProviderInfoErrorComponent |
            ApiV1DomainsDomainRegistrarsArchiveCreateProviderReferenceErrorComponent |
            ApiV1DomainsDomainRegistrarsArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1DomainsDomainRegistrarsArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1DomainsDomainRegistrarsArchiveCreateSlaTargetErrorComponent |
            ApiV1DomainsDomainRegistrarsArchiveCreateSlaWindowDaysErrorComponent |
            ApiV1DomainsDomainRegistrarsArchiveCreateSloAvailabilityErrorComponent |
            ApiV1DomainsDomainRegistrarsArchiveCreateSloTargetErrorComponent |
            ApiV1DomainsDomainRegistrarsArchiveCreateSloWindowDaysErrorComponent |
            ApiV1DomainsDomainRegistrarsArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1DomainsDomainRegistrarsArchiveCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1DomainsDomainRegistrarsArchiveCreateAnnotationsErrorComponent
        | ApiV1DomainsDomainRegistrarsArchiveCreateApiBackoffMinutesErrorComponent
        | ApiV1DomainsDomainRegistrarsArchiveCreateApiCredentialIdErrorComponent
        | ApiV1DomainsDomainRegistrarsArchiveCreateArchivedAtErrorComponent
        | ApiV1DomainsDomainRegistrarsArchiveCreateArchivedByErrorComponent
        | ApiV1DomainsDomainRegistrarsArchiveCreateArchivedErrorComponent
        | ApiV1DomainsDomainRegistrarsArchiveCreateArchivedReasonErrorComponent
        | ApiV1DomainsDomainRegistrarsArchiveCreateCreatedByComponentErrorComponent
        | ApiV1DomainsDomainRegistrarsArchiveCreateCreatedByUserErrorComponent
        | ApiV1DomainsDomainRegistrarsArchiveCreateCriticalityErrorComponent
        | ApiV1DomainsDomainRegistrarsArchiveCreateDebugModeErrorComponent
        | ApiV1DomainsDomainRegistrarsArchiveCreateDefaultRenewalModeErrorComponent
        | ApiV1DomainsDomainRegistrarsArchiveCreateDisplayNameErrorComponent
        | ApiV1DomainsDomainRegistrarsArchiveCreateImportContactsErrorComponent
        | ApiV1DomainsDomainRegistrarsArchiveCreateImportDomainsErrorComponent
        | ApiV1DomainsDomainRegistrarsArchiveCreateKindErrorComponent
        | ApiV1DomainsDomainRegistrarsArchiveCreateLabelsErrorComponent
        | ApiV1DomainsDomainRegistrarsArchiveCreateLastRateLimitedAtErrorComponent
        | ApiV1DomainsDomainRegistrarsArchiveCreateLastReconciliationDurationSecondsErrorComponent
        | ApiV1DomainsDomainRegistrarsArchiveCreateManagedByContentTypeErrorComponent
        | ApiV1DomainsDomainRegistrarsArchiveCreateManagedByObjectIdErrorComponent
        | ApiV1DomainsDomainRegistrarsArchiveCreateModifiedByUserErrorComponent
        | ApiV1DomainsDomainRegistrarsArchiveCreateNameErrorComponent
        | ApiV1DomainsDomainRegistrarsArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1DomainsDomainRegistrarsArchiveCreateOteErrorComponent
        | ApiV1DomainsDomainRegistrarsArchiveCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1DomainsDomainRegistrarsArchiveCreatePlatformServiceErrorComponent
        | ApiV1DomainsDomainRegistrarsArchiveCreateProviderErrorComponent
        | ApiV1DomainsDomainRegistrarsArchiveCreateProviderIdErrorComponent
        | ApiV1DomainsDomainRegistrarsArchiveCreateProviderInfoErrorComponent
        | ApiV1DomainsDomainRegistrarsArchiveCreateProviderReferenceErrorComponent
        | ApiV1DomainsDomainRegistrarsArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1DomainsDomainRegistrarsArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1DomainsDomainRegistrarsArchiveCreateSlaTargetErrorComponent
        | ApiV1DomainsDomainRegistrarsArchiveCreateSlaWindowDaysErrorComponent
        | ApiV1DomainsDomainRegistrarsArchiveCreateSloAvailabilityErrorComponent
        | ApiV1DomainsDomainRegistrarsArchiveCreateSloTargetErrorComponent
        | ApiV1DomainsDomainRegistrarsArchiveCreateSloWindowDaysErrorComponent
        | ApiV1DomainsDomainRegistrarsArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1DomainsDomainRegistrarsArchiveCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_domains_domain_registrars_archive_create_annotations_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_api_backoff_minutes_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateApiBackoffMinutesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_api_credential_id_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateApiCredentialIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_archived_at_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_archived_by_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_archived_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_archived_reason_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_created_by_component_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_criticality_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_debug_mode_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_default_renewal_mode_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateDefaultRenewalModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_display_name_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_import_contacts_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateImportContactsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_import_domains_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateImportDomainsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_kind_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_labels_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_last_rate_limited_at_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateLastRateLimitedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_managed_by_content_type_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_managed_by_object_id_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_modified_by_user_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_name_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_non_field_errors_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_ote_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateOteErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_platform_dns_record_created_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_platform_service_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_provider_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_provider_id_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_provider_info_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateProviderInfoErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_provider_reference_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_reconciliation_enabled_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_sla_availability_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_sla_target_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_sla_window_days_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_slo_availability_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_slo_target_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_slo_window_days_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_target_availability_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_tolerations_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsArchiveCreateApiCredentialIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1DomainsDomainRegistrarsArchiveCreateReconciliationEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data,
                ApiV1DomainsDomainRegistrarsArchiveCreateLastReconciliationDurationSecondsErrorComponent,
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1DomainsDomainRegistrarsArchiveCreateCreatedByComponentErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1DomainsDomainRegistrarsArchiveCreateTargetAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsArchiveCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsArchiveCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsArchiveCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1DomainsDomainRegistrarsArchiveCreatePlatformDnsRecordCreatedErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsArchiveCreateOteErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1DomainsDomainRegistrarsArchiveCreateDefaultRenewalModeErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsArchiveCreateImportDomainsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsArchiveCreateImportContactsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsArchiveCreateProviderInfoErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsArchiveCreateLastRateLimitedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsArchiveCreateApiBackoffMinutesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsArchiveCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1DomainsDomainRegistrarsArchiveCreateManagedByContentTypeErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsArchiveCreateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_domains_domain_registrars_archive_create_annotations_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_api_backoff_minutes_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateApiBackoffMinutesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_api_credential_id_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateApiCredentialIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_archived_at_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_archived_by_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_archived_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_archived_reason_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_created_by_component_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_created_by_user_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_criticality_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_debug_mode_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_default_renewal_mode_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateDefaultRenewalModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_display_name_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_import_contacts_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateImportContactsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_import_domains_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateImportDomainsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_kind_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_labels_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_last_rate_limited_at_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateLastRateLimitedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_managed_by_content_type_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_managed_by_object_id_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_modified_by_user_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_name_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_non_field_errors_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_ote_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateOteErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_platform_dns_record_created_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_platform_service_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_provider_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_provider_id_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_provider_info_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateProviderInfoErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_provider_reference_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_reconciliation_enabled_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_sla_availability_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_sla_target_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_sla_window_days_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_slo_availability_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_slo_target_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_slo_window_days_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_target_availability_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_archive_create_tolerations_error_component import (
            ApiV1DomainsDomainRegistrarsArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1DomainsDomainRegistrarsArchiveCreateAnnotationsErrorComponent
                | ApiV1DomainsDomainRegistrarsArchiveCreateApiBackoffMinutesErrorComponent
                | ApiV1DomainsDomainRegistrarsArchiveCreateApiCredentialIdErrorComponent
                | ApiV1DomainsDomainRegistrarsArchiveCreateArchivedAtErrorComponent
                | ApiV1DomainsDomainRegistrarsArchiveCreateArchivedByErrorComponent
                | ApiV1DomainsDomainRegistrarsArchiveCreateArchivedErrorComponent
                | ApiV1DomainsDomainRegistrarsArchiveCreateArchivedReasonErrorComponent
                | ApiV1DomainsDomainRegistrarsArchiveCreateCreatedByComponentErrorComponent
                | ApiV1DomainsDomainRegistrarsArchiveCreateCreatedByUserErrorComponent
                | ApiV1DomainsDomainRegistrarsArchiveCreateCriticalityErrorComponent
                | ApiV1DomainsDomainRegistrarsArchiveCreateDebugModeErrorComponent
                | ApiV1DomainsDomainRegistrarsArchiveCreateDefaultRenewalModeErrorComponent
                | ApiV1DomainsDomainRegistrarsArchiveCreateDisplayNameErrorComponent
                | ApiV1DomainsDomainRegistrarsArchiveCreateImportContactsErrorComponent
                | ApiV1DomainsDomainRegistrarsArchiveCreateImportDomainsErrorComponent
                | ApiV1DomainsDomainRegistrarsArchiveCreateKindErrorComponent
                | ApiV1DomainsDomainRegistrarsArchiveCreateLabelsErrorComponent
                | ApiV1DomainsDomainRegistrarsArchiveCreateLastRateLimitedAtErrorComponent
                | ApiV1DomainsDomainRegistrarsArchiveCreateLastReconciliationDurationSecondsErrorComponent
                | ApiV1DomainsDomainRegistrarsArchiveCreateManagedByContentTypeErrorComponent
                | ApiV1DomainsDomainRegistrarsArchiveCreateManagedByObjectIdErrorComponent
                | ApiV1DomainsDomainRegistrarsArchiveCreateModifiedByUserErrorComponent
                | ApiV1DomainsDomainRegistrarsArchiveCreateNameErrorComponent
                | ApiV1DomainsDomainRegistrarsArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1DomainsDomainRegistrarsArchiveCreateOteErrorComponent
                | ApiV1DomainsDomainRegistrarsArchiveCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1DomainsDomainRegistrarsArchiveCreatePlatformServiceErrorComponent
                | ApiV1DomainsDomainRegistrarsArchiveCreateProviderErrorComponent
                | ApiV1DomainsDomainRegistrarsArchiveCreateProviderIdErrorComponent
                | ApiV1DomainsDomainRegistrarsArchiveCreateProviderInfoErrorComponent
                | ApiV1DomainsDomainRegistrarsArchiveCreateProviderReferenceErrorComponent
                | ApiV1DomainsDomainRegistrarsArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1DomainsDomainRegistrarsArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1DomainsDomainRegistrarsArchiveCreateSlaTargetErrorComponent
                | ApiV1DomainsDomainRegistrarsArchiveCreateSlaWindowDaysErrorComponent
                | ApiV1DomainsDomainRegistrarsArchiveCreateSloAvailabilityErrorComponent
                | ApiV1DomainsDomainRegistrarsArchiveCreateSloTargetErrorComponent
                | ApiV1DomainsDomainRegistrarsArchiveCreateSloWindowDaysErrorComponent
                | ApiV1DomainsDomainRegistrarsArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1DomainsDomainRegistrarsArchiveCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_0 = (
                        ApiV1DomainsDomainRegistrarsArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_1 = (
                        ApiV1DomainsDomainRegistrarsArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_2 = (
                        ApiV1DomainsDomainRegistrarsArchiveCreateApiCredentialIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_3 = (
                        ApiV1DomainsDomainRegistrarsArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_4 = (
                        ApiV1DomainsDomainRegistrarsArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_5 = (
                        ApiV1DomainsDomainRegistrarsArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_6 = (
                        ApiV1DomainsDomainRegistrarsArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_7 = (
                        ApiV1DomainsDomainRegistrarsArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_8 = (
                        ApiV1DomainsDomainRegistrarsArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_9 = (
                        ApiV1DomainsDomainRegistrarsArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_10 = (
                        ApiV1DomainsDomainRegistrarsArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_11 = ApiV1DomainsDomainRegistrarsArchiveCreateLastReconciliationDurationSecondsErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_12 = (
                        ApiV1DomainsDomainRegistrarsArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_13 = (
                        ApiV1DomainsDomainRegistrarsArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_14 = (
                        ApiV1DomainsDomainRegistrarsArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_15 = (
                        ApiV1DomainsDomainRegistrarsArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_16 = (
                        ApiV1DomainsDomainRegistrarsArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_17 = (
                        ApiV1DomainsDomainRegistrarsArchiveCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_18 = (
                        ApiV1DomainsDomainRegistrarsArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_19 = (
                        ApiV1DomainsDomainRegistrarsArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_20 = (
                        ApiV1DomainsDomainRegistrarsArchiveCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_21 = (
                        ApiV1DomainsDomainRegistrarsArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_22 = (
                        ApiV1DomainsDomainRegistrarsArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_23 = (
                        ApiV1DomainsDomainRegistrarsArchiveCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_24 = (
                        ApiV1DomainsDomainRegistrarsArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_25 = (
                        ApiV1DomainsDomainRegistrarsArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_26 = (
                        ApiV1DomainsDomainRegistrarsArchiveCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_27 = (
                        ApiV1DomainsDomainRegistrarsArchiveCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_28 = (
                        ApiV1DomainsDomainRegistrarsArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_29 = (
                        ApiV1DomainsDomainRegistrarsArchiveCreateOteErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_30 = (
                        ApiV1DomainsDomainRegistrarsArchiveCreateDefaultRenewalModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_31 = (
                        ApiV1DomainsDomainRegistrarsArchiveCreateImportDomainsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_32 = (
                        ApiV1DomainsDomainRegistrarsArchiveCreateImportContactsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_33 = (
                        ApiV1DomainsDomainRegistrarsArchiveCreateProviderInfoErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_34 = (
                        ApiV1DomainsDomainRegistrarsArchiveCreateLastRateLimitedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_35 = (
                        ApiV1DomainsDomainRegistrarsArchiveCreateApiBackoffMinutesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_36 = (
                        ApiV1DomainsDomainRegistrarsArchiveCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_37 = (
                        ApiV1DomainsDomainRegistrarsArchiveCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_38 = (
                        ApiV1DomainsDomainRegistrarsArchiveCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_39 = (
                    ApiV1DomainsDomainRegistrarsArchiveCreateCreatedByUserErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_domains_domain_registrars_archive_create_error_type_39

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_domains_domain_registrars_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_domains_domain_registrars_archive_create_validation_error.additional_properties = d
        return api_v1_domains_domain_registrars_archive_create_validation_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
