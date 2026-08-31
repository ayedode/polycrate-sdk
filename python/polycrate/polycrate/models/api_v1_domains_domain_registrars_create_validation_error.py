from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_domains_domain_registrars_create_annotations_error_component import (
        ApiV1DomainsDomainRegistrarsCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_create_api_backoff_minutes_error_component import (
        ApiV1DomainsDomainRegistrarsCreateApiBackoffMinutesErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_create_api_credential_id_error_component import (
        ApiV1DomainsDomainRegistrarsCreateApiCredentialIdErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_create_archived_at_error_component import (
        ApiV1DomainsDomainRegistrarsCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_create_archived_by_error_component import (
        ApiV1DomainsDomainRegistrarsCreateArchivedByErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_create_archived_error_component import (
        ApiV1DomainsDomainRegistrarsCreateArchivedErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_create_archived_reason_error_component import (
        ApiV1DomainsDomainRegistrarsCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_create_created_by_component_error_component import (
        ApiV1DomainsDomainRegistrarsCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_create_created_by_user_error_component import (
        ApiV1DomainsDomainRegistrarsCreateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_create_criticality_error_component import (
        ApiV1DomainsDomainRegistrarsCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_create_debug_mode_error_component import (
        ApiV1DomainsDomainRegistrarsCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_create_default_renewal_mode_error_component import (
        ApiV1DomainsDomainRegistrarsCreateDefaultRenewalModeErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_create_display_name_error_component import (
        ApiV1DomainsDomainRegistrarsCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_create_import_contacts_error_component import (
        ApiV1DomainsDomainRegistrarsCreateImportContactsErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_create_import_domains_error_component import (
        ApiV1DomainsDomainRegistrarsCreateImportDomainsErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_create_kind_error_component import (
        ApiV1DomainsDomainRegistrarsCreateKindErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_create_labels_error_component import (
        ApiV1DomainsDomainRegistrarsCreateLabelsErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_create_last_rate_limited_at_error_component import (
        ApiV1DomainsDomainRegistrarsCreateLastRateLimitedAtErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_create_last_reconciliation_duration_seconds_error_component import (
        ApiV1DomainsDomainRegistrarsCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_create_managed_by_content_type_error_component import (
        ApiV1DomainsDomainRegistrarsCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_create_managed_by_object_id_error_component import (
        ApiV1DomainsDomainRegistrarsCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_create_modified_by_user_error_component import (
        ApiV1DomainsDomainRegistrarsCreateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_create_name_error_component import (
        ApiV1DomainsDomainRegistrarsCreateNameErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_create_non_field_errors_error_component import (
        ApiV1DomainsDomainRegistrarsCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_create_ote_error_component import (
        ApiV1DomainsDomainRegistrarsCreateOteErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_create_platform_dns_record_created_error_component import (
        ApiV1DomainsDomainRegistrarsCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_create_platform_service_error_component import (
        ApiV1DomainsDomainRegistrarsCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_create_provider_error_component import (
        ApiV1DomainsDomainRegistrarsCreateProviderErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_create_provider_id_error_component import (
        ApiV1DomainsDomainRegistrarsCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_create_provider_info_error_component import (
        ApiV1DomainsDomainRegistrarsCreateProviderInfoErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_create_provider_reference_error_component import (
        ApiV1DomainsDomainRegistrarsCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_create_reconciliation_enabled_error_component import (
        ApiV1DomainsDomainRegistrarsCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_create_sla_availability_error_component import (
        ApiV1DomainsDomainRegistrarsCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_create_sla_target_error_component import (
        ApiV1DomainsDomainRegistrarsCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_create_sla_window_days_error_component import (
        ApiV1DomainsDomainRegistrarsCreateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_create_slo_availability_error_component import (
        ApiV1DomainsDomainRegistrarsCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_create_slo_target_error_component import (
        ApiV1DomainsDomainRegistrarsCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_create_slo_window_days_error_component import (
        ApiV1DomainsDomainRegistrarsCreateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_create_target_availability_error_component import (
        ApiV1DomainsDomainRegistrarsCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_create_tolerations_error_component import (
        ApiV1DomainsDomainRegistrarsCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1DomainsDomainRegistrarsCreateValidationError")


@_attrs_define
class ApiV1DomainsDomainRegistrarsCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1DomainsDomainRegistrarsCreateAnnotationsErrorComponent |
            ApiV1DomainsDomainRegistrarsCreateApiBackoffMinutesErrorComponent |
            ApiV1DomainsDomainRegistrarsCreateApiCredentialIdErrorComponent |
            ApiV1DomainsDomainRegistrarsCreateArchivedAtErrorComponent |
            ApiV1DomainsDomainRegistrarsCreateArchivedByErrorComponent |
            ApiV1DomainsDomainRegistrarsCreateArchivedErrorComponent |
            ApiV1DomainsDomainRegistrarsCreateArchivedReasonErrorComponent |
            ApiV1DomainsDomainRegistrarsCreateCreatedByComponentErrorComponent |
            ApiV1DomainsDomainRegistrarsCreateCreatedByUserErrorComponent |
            ApiV1DomainsDomainRegistrarsCreateCriticalityErrorComponent |
            ApiV1DomainsDomainRegistrarsCreateDebugModeErrorComponent |
            ApiV1DomainsDomainRegistrarsCreateDefaultRenewalModeErrorComponent |
            ApiV1DomainsDomainRegistrarsCreateDisplayNameErrorComponent |
            ApiV1DomainsDomainRegistrarsCreateImportContactsErrorComponent |
            ApiV1DomainsDomainRegistrarsCreateImportDomainsErrorComponent |
            ApiV1DomainsDomainRegistrarsCreateKindErrorComponent | ApiV1DomainsDomainRegistrarsCreateLabelsErrorComponent |
            ApiV1DomainsDomainRegistrarsCreateLastRateLimitedAtErrorComponent |
            ApiV1DomainsDomainRegistrarsCreateLastReconciliationDurationSecondsErrorComponent |
            ApiV1DomainsDomainRegistrarsCreateManagedByContentTypeErrorComponent |
            ApiV1DomainsDomainRegistrarsCreateManagedByObjectIdErrorComponent |
            ApiV1DomainsDomainRegistrarsCreateModifiedByUserErrorComponent |
            ApiV1DomainsDomainRegistrarsCreateNameErrorComponent |
            ApiV1DomainsDomainRegistrarsCreateNonFieldErrorsErrorComponent |
            ApiV1DomainsDomainRegistrarsCreateOteErrorComponent |
            ApiV1DomainsDomainRegistrarsCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1DomainsDomainRegistrarsCreatePlatformServiceErrorComponent |
            ApiV1DomainsDomainRegistrarsCreateProviderErrorComponent |
            ApiV1DomainsDomainRegistrarsCreateProviderIdErrorComponent |
            ApiV1DomainsDomainRegistrarsCreateProviderInfoErrorComponent |
            ApiV1DomainsDomainRegistrarsCreateProviderReferenceErrorComponent |
            ApiV1DomainsDomainRegistrarsCreateReconciliationEnabledErrorComponent |
            ApiV1DomainsDomainRegistrarsCreateSlaAvailabilityErrorComponent |
            ApiV1DomainsDomainRegistrarsCreateSlaTargetErrorComponent |
            ApiV1DomainsDomainRegistrarsCreateSlaWindowDaysErrorComponent |
            ApiV1DomainsDomainRegistrarsCreateSloAvailabilityErrorComponent |
            ApiV1DomainsDomainRegistrarsCreateSloTargetErrorComponent |
            ApiV1DomainsDomainRegistrarsCreateSloWindowDaysErrorComponent |
            ApiV1DomainsDomainRegistrarsCreateTargetAvailabilityErrorComponent |
            ApiV1DomainsDomainRegistrarsCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1DomainsDomainRegistrarsCreateAnnotationsErrorComponent
        | ApiV1DomainsDomainRegistrarsCreateApiBackoffMinutesErrorComponent
        | ApiV1DomainsDomainRegistrarsCreateApiCredentialIdErrorComponent
        | ApiV1DomainsDomainRegistrarsCreateArchivedAtErrorComponent
        | ApiV1DomainsDomainRegistrarsCreateArchivedByErrorComponent
        | ApiV1DomainsDomainRegistrarsCreateArchivedErrorComponent
        | ApiV1DomainsDomainRegistrarsCreateArchivedReasonErrorComponent
        | ApiV1DomainsDomainRegistrarsCreateCreatedByComponentErrorComponent
        | ApiV1DomainsDomainRegistrarsCreateCreatedByUserErrorComponent
        | ApiV1DomainsDomainRegistrarsCreateCriticalityErrorComponent
        | ApiV1DomainsDomainRegistrarsCreateDebugModeErrorComponent
        | ApiV1DomainsDomainRegistrarsCreateDefaultRenewalModeErrorComponent
        | ApiV1DomainsDomainRegistrarsCreateDisplayNameErrorComponent
        | ApiV1DomainsDomainRegistrarsCreateImportContactsErrorComponent
        | ApiV1DomainsDomainRegistrarsCreateImportDomainsErrorComponent
        | ApiV1DomainsDomainRegistrarsCreateKindErrorComponent
        | ApiV1DomainsDomainRegistrarsCreateLabelsErrorComponent
        | ApiV1DomainsDomainRegistrarsCreateLastRateLimitedAtErrorComponent
        | ApiV1DomainsDomainRegistrarsCreateLastReconciliationDurationSecondsErrorComponent
        | ApiV1DomainsDomainRegistrarsCreateManagedByContentTypeErrorComponent
        | ApiV1DomainsDomainRegistrarsCreateManagedByObjectIdErrorComponent
        | ApiV1DomainsDomainRegistrarsCreateModifiedByUserErrorComponent
        | ApiV1DomainsDomainRegistrarsCreateNameErrorComponent
        | ApiV1DomainsDomainRegistrarsCreateNonFieldErrorsErrorComponent
        | ApiV1DomainsDomainRegistrarsCreateOteErrorComponent
        | ApiV1DomainsDomainRegistrarsCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1DomainsDomainRegistrarsCreatePlatformServiceErrorComponent
        | ApiV1DomainsDomainRegistrarsCreateProviderErrorComponent
        | ApiV1DomainsDomainRegistrarsCreateProviderIdErrorComponent
        | ApiV1DomainsDomainRegistrarsCreateProviderInfoErrorComponent
        | ApiV1DomainsDomainRegistrarsCreateProviderReferenceErrorComponent
        | ApiV1DomainsDomainRegistrarsCreateReconciliationEnabledErrorComponent
        | ApiV1DomainsDomainRegistrarsCreateSlaAvailabilityErrorComponent
        | ApiV1DomainsDomainRegistrarsCreateSlaTargetErrorComponent
        | ApiV1DomainsDomainRegistrarsCreateSlaWindowDaysErrorComponent
        | ApiV1DomainsDomainRegistrarsCreateSloAvailabilityErrorComponent
        | ApiV1DomainsDomainRegistrarsCreateSloTargetErrorComponent
        | ApiV1DomainsDomainRegistrarsCreateSloWindowDaysErrorComponent
        | ApiV1DomainsDomainRegistrarsCreateTargetAvailabilityErrorComponent
        | ApiV1DomainsDomainRegistrarsCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_domains_domain_registrars_create_annotations_error_component import (
            ApiV1DomainsDomainRegistrarsCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_api_backoff_minutes_error_component import (
            ApiV1DomainsDomainRegistrarsCreateApiBackoffMinutesErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_api_credential_id_error_component import (
            ApiV1DomainsDomainRegistrarsCreateApiCredentialIdErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_archived_at_error_component import (
            ApiV1DomainsDomainRegistrarsCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_archived_by_error_component import (
            ApiV1DomainsDomainRegistrarsCreateArchivedByErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_archived_error_component import (
            ApiV1DomainsDomainRegistrarsCreateArchivedErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_archived_reason_error_component import (
            ApiV1DomainsDomainRegistrarsCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_created_by_component_error_component import (
            ApiV1DomainsDomainRegistrarsCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_criticality_error_component import (
            ApiV1DomainsDomainRegistrarsCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_debug_mode_error_component import (
            ApiV1DomainsDomainRegistrarsCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_default_renewal_mode_error_component import (
            ApiV1DomainsDomainRegistrarsCreateDefaultRenewalModeErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_display_name_error_component import (
            ApiV1DomainsDomainRegistrarsCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_import_contacts_error_component import (
            ApiV1DomainsDomainRegistrarsCreateImportContactsErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_import_domains_error_component import (
            ApiV1DomainsDomainRegistrarsCreateImportDomainsErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_kind_error_component import (
            ApiV1DomainsDomainRegistrarsCreateKindErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_labels_error_component import (
            ApiV1DomainsDomainRegistrarsCreateLabelsErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_last_rate_limited_at_error_component import (
            ApiV1DomainsDomainRegistrarsCreateLastRateLimitedAtErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1DomainsDomainRegistrarsCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_managed_by_content_type_error_component import (
            ApiV1DomainsDomainRegistrarsCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_managed_by_object_id_error_component import (
            ApiV1DomainsDomainRegistrarsCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_modified_by_user_error_component import (
            ApiV1DomainsDomainRegistrarsCreateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_name_error_component import (
            ApiV1DomainsDomainRegistrarsCreateNameErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_non_field_errors_error_component import (
            ApiV1DomainsDomainRegistrarsCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_ote_error_component import (
            ApiV1DomainsDomainRegistrarsCreateOteErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_platform_dns_record_created_error_component import (
            ApiV1DomainsDomainRegistrarsCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_platform_service_error_component import (
            ApiV1DomainsDomainRegistrarsCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_provider_error_component import (
            ApiV1DomainsDomainRegistrarsCreateProviderErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_provider_id_error_component import (
            ApiV1DomainsDomainRegistrarsCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_provider_info_error_component import (
            ApiV1DomainsDomainRegistrarsCreateProviderInfoErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_provider_reference_error_component import (
            ApiV1DomainsDomainRegistrarsCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_reconciliation_enabled_error_component import (
            ApiV1DomainsDomainRegistrarsCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_sla_availability_error_component import (
            ApiV1DomainsDomainRegistrarsCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_sla_target_error_component import (
            ApiV1DomainsDomainRegistrarsCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_sla_window_days_error_component import (
            ApiV1DomainsDomainRegistrarsCreateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_slo_availability_error_component import (
            ApiV1DomainsDomainRegistrarsCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_slo_target_error_component import (
            ApiV1DomainsDomainRegistrarsCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_slo_window_days_error_component import (
            ApiV1DomainsDomainRegistrarsCreateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_target_availability_error_component import (
            ApiV1DomainsDomainRegistrarsCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_tolerations_error_component import (
            ApiV1DomainsDomainRegistrarsCreateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsCreateApiCredentialIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1DomainsDomainRegistrarsCreateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsCreatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsCreateOteErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsCreateDefaultRenewalModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsCreateImportDomainsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsCreateImportContactsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsCreateProviderInfoErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsCreateLastRateLimitedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsCreateApiBackoffMinutesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsCreateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsCreateModifiedByUserErrorComponent):
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
        from ..models.api_v1_domains_domain_registrars_create_annotations_error_component import (
            ApiV1DomainsDomainRegistrarsCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_api_backoff_minutes_error_component import (
            ApiV1DomainsDomainRegistrarsCreateApiBackoffMinutesErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_api_credential_id_error_component import (
            ApiV1DomainsDomainRegistrarsCreateApiCredentialIdErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_archived_at_error_component import (
            ApiV1DomainsDomainRegistrarsCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_archived_by_error_component import (
            ApiV1DomainsDomainRegistrarsCreateArchivedByErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_archived_error_component import (
            ApiV1DomainsDomainRegistrarsCreateArchivedErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_archived_reason_error_component import (
            ApiV1DomainsDomainRegistrarsCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_created_by_component_error_component import (
            ApiV1DomainsDomainRegistrarsCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_created_by_user_error_component import (
            ApiV1DomainsDomainRegistrarsCreateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_criticality_error_component import (
            ApiV1DomainsDomainRegistrarsCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_debug_mode_error_component import (
            ApiV1DomainsDomainRegistrarsCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_default_renewal_mode_error_component import (
            ApiV1DomainsDomainRegistrarsCreateDefaultRenewalModeErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_display_name_error_component import (
            ApiV1DomainsDomainRegistrarsCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_import_contacts_error_component import (
            ApiV1DomainsDomainRegistrarsCreateImportContactsErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_import_domains_error_component import (
            ApiV1DomainsDomainRegistrarsCreateImportDomainsErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_kind_error_component import (
            ApiV1DomainsDomainRegistrarsCreateKindErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_labels_error_component import (
            ApiV1DomainsDomainRegistrarsCreateLabelsErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_last_rate_limited_at_error_component import (
            ApiV1DomainsDomainRegistrarsCreateLastRateLimitedAtErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1DomainsDomainRegistrarsCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_managed_by_content_type_error_component import (
            ApiV1DomainsDomainRegistrarsCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_managed_by_object_id_error_component import (
            ApiV1DomainsDomainRegistrarsCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_modified_by_user_error_component import (
            ApiV1DomainsDomainRegistrarsCreateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_name_error_component import (
            ApiV1DomainsDomainRegistrarsCreateNameErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_non_field_errors_error_component import (
            ApiV1DomainsDomainRegistrarsCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_ote_error_component import (
            ApiV1DomainsDomainRegistrarsCreateOteErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_platform_dns_record_created_error_component import (
            ApiV1DomainsDomainRegistrarsCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_platform_service_error_component import (
            ApiV1DomainsDomainRegistrarsCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_provider_error_component import (
            ApiV1DomainsDomainRegistrarsCreateProviderErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_provider_id_error_component import (
            ApiV1DomainsDomainRegistrarsCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_provider_info_error_component import (
            ApiV1DomainsDomainRegistrarsCreateProviderInfoErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_provider_reference_error_component import (
            ApiV1DomainsDomainRegistrarsCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_reconciliation_enabled_error_component import (
            ApiV1DomainsDomainRegistrarsCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_sla_availability_error_component import (
            ApiV1DomainsDomainRegistrarsCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_sla_target_error_component import (
            ApiV1DomainsDomainRegistrarsCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_sla_window_days_error_component import (
            ApiV1DomainsDomainRegistrarsCreateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_slo_availability_error_component import (
            ApiV1DomainsDomainRegistrarsCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_slo_target_error_component import (
            ApiV1DomainsDomainRegistrarsCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_slo_window_days_error_component import (
            ApiV1DomainsDomainRegistrarsCreateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_target_availability_error_component import (
            ApiV1DomainsDomainRegistrarsCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_domains_domain_registrars_create_tolerations_error_component import (
            ApiV1DomainsDomainRegistrarsCreateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1DomainsDomainRegistrarsCreateAnnotationsErrorComponent
                | ApiV1DomainsDomainRegistrarsCreateApiBackoffMinutesErrorComponent
                | ApiV1DomainsDomainRegistrarsCreateApiCredentialIdErrorComponent
                | ApiV1DomainsDomainRegistrarsCreateArchivedAtErrorComponent
                | ApiV1DomainsDomainRegistrarsCreateArchivedByErrorComponent
                | ApiV1DomainsDomainRegistrarsCreateArchivedErrorComponent
                | ApiV1DomainsDomainRegistrarsCreateArchivedReasonErrorComponent
                | ApiV1DomainsDomainRegistrarsCreateCreatedByComponentErrorComponent
                | ApiV1DomainsDomainRegistrarsCreateCreatedByUserErrorComponent
                | ApiV1DomainsDomainRegistrarsCreateCriticalityErrorComponent
                | ApiV1DomainsDomainRegistrarsCreateDebugModeErrorComponent
                | ApiV1DomainsDomainRegistrarsCreateDefaultRenewalModeErrorComponent
                | ApiV1DomainsDomainRegistrarsCreateDisplayNameErrorComponent
                | ApiV1DomainsDomainRegistrarsCreateImportContactsErrorComponent
                | ApiV1DomainsDomainRegistrarsCreateImportDomainsErrorComponent
                | ApiV1DomainsDomainRegistrarsCreateKindErrorComponent
                | ApiV1DomainsDomainRegistrarsCreateLabelsErrorComponent
                | ApiV1DomainsDomainRegistrarsCreateLastRateLimitedAtErrorComponent
                | ApiV1DomainsDomainRegistrarsCreateLastReconciliationDurationSecondsErrorComponent
                | ApiV1DomainsDomainRegistrarsCreateManagedByContentTypeErrorComponent
                | ApiV1DomainsDomainRegistrarsCreateManagedByObjectIdErrorComponent
                | ApiV1DomainsDomainRegistrarsCreateModifiedByUserErrorComponent
                | ApiV1DomainsDomainRegistrarsCreateNameErrorComponent
                | ApiV1DomainsDomainRegistrarsCreateNonFieldErrorsErrorComponent
                | ApiV1DomainsDomainRegistrarsCreateOteErrorComponent
                | ApiV1DomainsDomainRegistrarsCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1DomainsDomainRegistrarsCreatePlatformServiceErrorComponent
                | ApiV1DomainsDomainRegistrarsCreateProviderErrorComponent
                | ApiV1DomainsDomainRegistrarsCreateProviderIdErrorComponent
                | ApiV1DomainsDomainRegistrarsCreateProviderInfoErrorComponent
                | ApiV1DomainsDomainRegistrarsCreateProviderReferenceErrorComponent
                | ApiV1DomainsDomainRegistrarsCreateReconciliationEnabledErrorComponent
                | ApiV1DomainsDomainRegistrarsCreateSlaAvailabilityErrorComponent
                | ApiV1DomainsDomainRegistrarsCreateSlaTargetErrorComponent
                | ApiV1DomainsDomainRegistrarsCreateSlaWindowDaysErrorComponent
                | ApiV1DomainsDomainRegistrarsCreateSloAvailabilityErrorComponent
                | ApiV1DomainsDomainRegistrarsCreateSloTargetErrorComponent
                | ApiV1DomainsDomainRegistrarsCreateSloWindowDaysErrorComponent
                | ApiV1DomainsDomainRegistrarsCreateTargetAvailabilityErrorComponent
                | ApiV1DomainsDomainRegistrarsCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_create_error_type_0 = (
                        ApiV1DomainsDomainRegistrarsCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_create_error_type_1 = (
                        ApiV1DomainsDomainRegistrarsCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_create_error_type_2 = (
                        ApiV1DomainsDomainRegistrarsCreateApiCredentialIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_create_error_type_3 = (
                        ApiV1DomainsDomainRegistrarsCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_create_error_type_4 = (
                        ApiV1DomainsDomainRegistrarsCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_create_error_type_5 = (
                        ApiV1DomainsDomainRegistrarsCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_create_error_type_6 = (
                        ApiV1DomainsDomainRegistrarsCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_create_error_type_7 = (
                        ApiV1DomainsDomainRegistrarsCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_create_error_type_8 = (
                        ApiV1DomainsDomainRegistrarsCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_create_error_type_9 = (
                        ApiV1DomainsDomainRegistrarsCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_create_error_type_10 = (
                        ApiV1DomainsDomainRegistrarsCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_create_error_type_11 = (
                        ApiV1DomainsDomainRegistrarsCreateLastReconciliationDurationSecondsErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_create_error_type_12 = (
                        ApiV1DomainsDomainRegistrarsCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_create_error_type_13 = (
                        ApiV1DomainsDomainRegistrarsCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_create_error_type_14 = (
                        ApiV1DomainsDomainRegistrarsCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_create_error_type_15 = (
                        ApiV1DomainsDomainRegistrarsCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_create_error_type_16 = (
                        ApiV1DomainsDomainRegistrarsCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_create_error_type_17 = (
                        ApiV1DomainsDomainRegistrarsCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_create_error_type_18 = (
                        ApiV1DomainsDomainRegistrarsCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_create_error_type_19 = (
                        ApiV1DomainsDomainRegistrarsCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_create_error_type_20 = (
                        ApiV1DomainsDomainRegistrarsCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_create_error_type_21 = (
                        ApiV1DomainsDomainRegistrarsCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_create_error_type_22 = (
                        ApiV1DomainsDomainRegistrarsCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_create_error_type_23 = (
                        ApiV1DomainsDomainRegistrarsCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_create_error_type_24 = (
                        ApiV1DomainsDomainRegistrarsCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_create_error_type_25 = (
                        ApiV1DomainsDomainRegistrarsCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_create_error_type_26 = (
                        ApiV1DomainsDomainRegistrarsCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_create_error_type_27 = (
                        ApiV1DomainsDomainRegistrarsCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_create_error_type_28 = (
                        ApiV1DomainsDomainRegistrarsCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_create_error_type_29 = (
                        ApiV1DomainsDomainRegistrarsCreateOteErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_create_error_type_30 = (
                        ApiV1DomainsDomainRegistrarsCreateDefaultRenewalModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_create_error_type_31 = (
                        ApiV1DomainsDomainRegistrarsCreateImportDomainsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_create_error_type_32 = (
                        ApiV1DomainsDomainRegistrarsCreateImportContactsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_create_error_type_33 = (
                        ApiV1DomainsDomainRegistrarsCreateProviderInfoErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_create_error_type_34 = (
                        ApiV1DomainsDomainRegistrarsCreateLastRateLimitedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_create_error_type_35 = (
                        ApiV1DomainsDomainRegistrarsCreateApiBackoffMinutesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_create_error_type_36 = (
                        ApiV1DomainsDomainRegistrarsCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_create_error_type_37 = (
                        ApiV1DomainsDomainRegistrarsCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_create_error_type_38 = (
                        ApiV1DomainsDomainRegistrarsCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_domains_domain_registrars_create_error_type_39 = (
                    ApiV1DomainsDomainRegistrarsCreateCreatedByUserErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_domains_domain_registrars_create_error_type_39

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_domains_domain_registrars_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_domains_domain_registrars_create_validation_error.additional_properties = d
        return api_v1_domains_domain_registrars_create_validation_error

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
