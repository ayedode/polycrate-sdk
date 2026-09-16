from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_domains_domain_registrars_partial_update_annotations_error_component import (
        ApiV1DomainsDomainRegistrarsPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_partial_update_api_backoff_minutes_error_component import (
        ApiV1DomainsDomainRegistrarsPartialUpdateApiBackoffMinutesErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_partial_update_api_credential_id_error_component import (
        ApiV1DomainsDomainRegistrarsPartialUpdateApiCredentialIdErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_partial_update_archived_at_error_component import (
        ApiV1DomainsDomainRegistrarsPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_partial_update_archived_by_error_component import (
        ApiV1DomainsDomainRegistrarsPartialUpdateArchivedByErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_partial_update_archived_error_component import (
        ApiV1DomainsDomainRegistrarsPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_partial_update_archived_reason_error_component import (
        ApiV1DomainsDomainRegistrarsPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_partial_update_created_by_component_error_component import (
        ApiV1DomainsDomainRegistrarsPartialUpdateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_partial_update_created_by_user_error_component import (
        ApiV1DomainsDomainRegistrarsPartialUpdateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_partial_update_criticality_error_component import (
        ApiV1DomainsDomainRegistrarsPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_partial_update_debug_mode_error_component import (
        ApiV1DomainsDomainRegistrarsPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_partial_update_default_renewal_mode_error_component import (
        ApiV1DomainsDomainRegistrarsPartialUpdateDefaultRenewalModeErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_partial_update_display_name_error_component import (
        ApiV1DomainsDomainRegistrarsPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_partial_update_import_contacts_error_component import (
        ApiV1DomainsDomainRegistrarsPartialUpdateImportContactsErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_partial_update_import_domains_error_component import (
        ApiV1DomainsDomainRegistrarsPartialUpdateImportDomainsErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_partial_update_kind_error_component import (
        ApiV1DomainsDomainRegistrarsPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_partial_update_labels_error_component import (
        ApiV1DomainsDomainRegistrarsPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_partial_update_last_rate_limited_at_error_component import (
        ApiV1DomainsDomainRegistrarsPartialUpdateLastRateLimitedAtErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_partial_update_last_reconciliation_duration_seconds_error_component import (
        ApiV1DomainsDomainRegistrarsPartialUpdateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_partial_update_managed_by_content_type_error_component import (
        ApiV1DomainsDomainRegistrarsPartialUpdateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_partial_update_managed_by_object_id_error_component import (
        ApiV1DomainsDomainRegistrarsPartialUpdateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_partial_update_modified_by_user_error_component import (
        ApiV1DomainsDomainRegistrarsPartialUpdateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_partial_update_name_error_component import (
        ApiV1DomainsDomainRegistrarsPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_partial_update_non_field_errors_error_component import (
        ApiV1DomainsDomainRegistrarsPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_partial_update_ote_error_component import (
        ApiV1DomainsDomainRegistrarsPartialUpdateOteErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_partial_update_platform_dns_record_created_error_component import (
        ApiV1DomainsDomainRegistrarsPartialUpdatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_partial_update_platform_service_error_component import (
        ApiV1DomainsDomainRegistrarsPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_partial_update_provider_error_component import (
        ApiV1DomainsDomainRegistrarsPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_partial_update_provider_id_error_component import (
        ApiV1DomainsDomainRegistrarsPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_partial_update_provider_info_error_component import (
        ApiV1DomainsDomainRegistrarsPartialUpdateProviderInfoErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_partial_update_provider_reference_error_component import (
        ApiV1DomainsDomainRegistrarsPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_partial_update_reconciliation_enabled_error_component import (
        ApiV1DomainsDomainRegistrarsPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_partial_update_sla_availability_error_component import (
        ApiV1DomainsDomainRegistrarsPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_partial_update_sla_target_error_component import (
        ApiV1DomainsDomainRegistrarsPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_partial_update_sla_window_days_error_component import (
        ApiV1DomainsDomainRegistrarsPartialUpdateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_partial_update_slo_availability_error_component import (
        ApiV1DomainsDomainRegistrarsPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_partial_update_slo_target_error_component import (
        ApiV1DomainsDomainRegistrarsPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_partial_update_slo_window_days_error_component import (
        ApiV1DomainsDomainRegistrarsPartialUpdateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_partial_update_target_availability_error_component import (
        ApiV1DomainsDomainRegistrarsPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_partial_update_tolerations_error_component import (
        ApiV1DomainsDomainRegistrarsPartialUpdateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1DomainsDomainRegistrarsPartialUpdateValidationError")


@_attrs_define
class ApiV1DomainsDomainRegistrarsPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1DomainsDomainRegistrarsPartialUpdateAnnotationsErrorComponent |
            ApiV1DomainsDomainRegistrarsPartialUpdateApiBackoffMinutesErrorComponent |
            ApiV1DomainsDomainRegistrarsPartialUpdateApiCredentialIdErrorComponent |
            ApiV1DomainsDomainRegistrarsPartialUpdateArchivedAtErrorComponent |
            ApiV1DomainsDomainRegistrarsPartialUpdateArchivedByErrorComponent |
            ApiV1DomainsDomainRegistrarsPartialUpdateArchivedErrorComponent |
            ApiV1DomainsDomainRegistrarsPartialUpdateArchivedReasonErrorComponent |
            ApiV1DomainsDomainRegistrarsPartialUpdateCreatedByComponentErrorComponent |
            ApiV1DomainsDomainRegistrarsPartialUpdateCreatedByUserErrorComponent |
            ApiV1DomainsDomainRegistrarsPartialUpdateCriticalityErrorComponent |
            ApiV1DomainsDomainRegistrarsPartialUpdateDebugModeErrorComponent |
            ApiV1DomainsDomainRegistrarsPartialUpdateDefaultRenewalModeErrorComponent |
            ApiV1DomainsDomainRegistrarsPartialUpdateDisplayNameErrorComponent |
            ApiV1DomainsDomainRegistrarsPartialUpdateImportContactsErrorComponent |
            ApiV1DomainsDomainRegistrarsPartialUpdateImportDomainsErrorComponent |
            ApiV1DomainsDomainRegistrarsPartialUpdateKindErrorComponent |
            ApiV1DomainsDomainRegistrarsPartialUpdateLabelsErrorComponent |
            ApiV1DomainsDomainRegistrarsPartialUpdateLastRateLimitedAtErrorComponent |
            ApiV1DomainsDomainRegistrarsPartialUpdateLastReconciliationDurationSecondsErrorComponent |
            ApiV1DomainsDomainRegistrarsPartialUpdateManagedByContentTypeErrorComponent |
            ApiV1DomainsDomainRegistrarsPartialUpdateManagedByObjectIdErrorComponent |
            ApiV1DomainsDomainRegistrarsPartialUpdateModifiedByUserErrorComponent |
            ApiV1DomainsDomainRegistrarsPartialUpdateNameErrorComponent |
            ApiV1DomainsDomainRegistrarsPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1DomainsDomainRegistrarsPartialUpdateOteErrorComponent |
            ApiV1DomainsDomainRegistrarsPartialUpdatePlatformDnsRecordCreatedErrorComponent |
            ApiV1DomainsDomainRegistrarsPartialUpdatePlatformServiceErrorComponent |
            ApiV1DomainsDomainRegistrarsPartialUpdateProviderErrorComponent |
            ApiV1DomainsDomainRegistrarsPartialUpdateProviderIdErrorComponent |
            ApiV1DomainsDomainRegistrarsPartialUpdateProviderInfoErrorComponent |
            ApiV1DomainsDomainRegistrarsPartialUpdateProviderReferenceErrorComponent |
            ApiV1DomainsDomainRegistrarsPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1DomainsDomainRegistrarsPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1DomainsDomainRegistrarsPartialUpdateSlaTargetErrorComponent |
            ApiV1DomainsDomainRegistrarsPartialUpdateSlaWindowDaysErrorComponent |
            ApiV1DomainsDomainRegistrarsPartialUpdateSloAvailabilityErrorComponent |
            ApiV1DomainsDomainRegistrarsPartialUpdateSloTargetErrorComponent |
            ApiV1DomainsDomainRegistrarsPartialUpdateSloWindowDaysErrorComponent |
            ApiV1DomainsDomainRegistrarsPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1DomainsDomainRegistrarsPartialUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1DomainsDomainRegistrarsPartialUpdateAnnotationsErrorComponent
        | ApiV1DomainsDomainRegistrarsPartialUpdateApiBackoffMinutesErrorComponent
        | ApiV1DomainsDomainRegistrarsPartialUpdateApiCredentialIdErrorComponent
        | ApiV1DomainsDomainRegistrarsPartialUpdateArchivedAtErrorComponent
        | ApiV1DomainsDomainRegistrarsPartialUpdateArchivedByErrorComponent
        | ApiV1DomainsDomainRegistrarsPartialUpdateArchivedErrorComponent
        | ApiV1DomainsDomainRegistrarsPartialUpdateArchivedReasonErrorComponent
        | ApiV1DomainsDomainRegistrarsPartialUpdateCreatedByComponentErrorComponent
        | ApiV1DomainsDomainRegistrarsPartialUpdateCreatedByUserErrorComponent
        | ApiV1DomainsDomainRegistrarsPartialUpdateCriticalityErrorComponent
        | ApiV1DomainsDomainRegistrarsPartialUpdateDebugModeErrorComponent
        | ApiV1DomainsDomainRegistrarsPartialUpdateDefaultRenewalModeErrorComponent
        | ApiV1DomainsDomainRegistrarsPartialUpdateDisplayNameErrorComponent
        | ApiV1DomainsDomainRegistrarsPartialUpdateImportContactsErrorComponent
        | ApiV1DomainsDomainRegistrarsPartialUpdateImportDomainsErrorComponent
        | ApiV1DomainsDomainRegistrarsPartialUpdateKindErrorComponent
        | ApiV1DomainsDomainRegistrarsPartialUpdateLabelsErrorComponent
        | ApiV1DomainsDomainRegistrarsPartialUpdateLastRateLimitedAtErrorComponent
        | ApiV1DomainsDomainRegistrarsPartialUpdateLastReconciliationDurationSecondsErrorComponent
        | ApiV1DomainsDomainRegistrarsPartialUpdateManagedByContentTypeErrorComponent
        | ApiV1DomainsDomainRegistrarsPartialUpdateManagedByObjectIdErrorComponent
        | ApiV1DomainsDomainRegistrarsPartialUpdateModifiedByUserErrorComponent
        | ApiV1DomainsDomainRegistrarsPartialUpdateNameErrorComponent
        | ApiV1DomainsDomainRegistrarsPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1DomainsDomainRegistrarsPartialUpdateOteErrorComponent
        | ApiV1DomainsDomainRegistrarsPartialUpdatePlatformDnsRecordCreatedErrorComponent
        | ApiV1DomainsDomainRegistrarsPartialUpdatePlatformServiceErrorComponent
        | ApiV1DomainsDomainRegistrarsPartialUpdateProviderErrorComponent
        | ApiV1DomainsDomainRegistrarsPartialUpdateProviderIdErrorComponent
        | ApiV1DomainsDomainRegistrarsPartialUpdateProviderInfoErrorComponent
        | ApiV1DomainsDomainRegistrarsPartialUpdateProviderReferenceErrorComponent
        | ApiV1DomainsDomainRegistrarsPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1DomainsDomainRegistrarsPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1DomainsDomainRegistrarsPartialUpdateSlaTargetErrorComponent
        | ApiV1DomainsDomainRegistrarsPartialUpdateSlaWindowDaysErrorComponent
        | ApiV1DomainsDomainRegistrarsPartialUpdateSloAvailabilityErrorComponent
        | ApiV1DomainsDomainRegistrarsPartialUpdateSloTargetErrorComponent
        | ApiV1DomainsDomainRegistrarsPartialUpdateSloWindowDaysErrorComponent
        | ApiV1DomainsDomainRegistrarsPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1DomainsDomainRegistrarsPartialUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_domains_domain_registrars_partial_update_annotations_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_api_backoff_minutes_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateApiBackoffMinutesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_api_credential_id_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateApiCredentialIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_archived_at_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_archived_by_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_archived_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_archived_reason_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_created_by_component_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_criticality_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_debug_mode_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_default_renewal_mode_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateDefaultRenewalModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_display_name_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_import_contacts_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateImportContactsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_import_domains_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateImportDomainsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_kind_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_labels_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_last_rate_limited_at_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateLastRateLimitedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_managed_by_content_type_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_managed_by_object_id_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_modified_by_user_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_name_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_non_field_errors_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_ote_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateOteErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_platform_dns_record_created_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_platform_service_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_provider_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_provider_id_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_provider_info_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateProviderInfoErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_provider_reference_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_reconciliation_enabled_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_sla_availability_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_sla_target_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_sla_window_days_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_slo_availability_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_slo_target_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_slo_window_days_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_target_availability_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_tolerations_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsPartialUpdateApiCredentialIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1DomainsDomainRegistrarsPartialUpdateReconciliationEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data,
                ApiV1DomainsDomainRegistrarsPartialUpdateLastReconciliationDurationSecondsErrorComponent,
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsPartialUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1DomainsDomainRegistrarsPartialUpdateCreatedByComponentErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1DomainsDomainRegistrarsPartialUpdateTargetAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsPartialUpdateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsPartialUpdateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsPartialUpdateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1DomainsDomainRegistrarsPartialUpdatePlatformDnsRecordCreatedErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsPartialUpdateOteErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1DomainsDomainRegistrarsPartialUpdateDefaultRenewalModeErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsPartialUpdateImportDomainsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsPartialUpdateImportContactsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsPartialUpdateProviderInfoErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsPartialUpdateLastRateLimitedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsPartialUpdateApiBackoffMinutesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsPartialUpdateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1DomainsDomainRegistrarsPartialUpdateManagedByContentTypeErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsPartialUpdateModifiedByUserErrorComponent):
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
        from ..models.api_v1_domains_domain_registrars_partial_update_annotations_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_api_backoff_minutes_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateApiBackoffMinutesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_api_credential_id_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateApiCredentialIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_archived_at_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_archived_by_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_archived_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_archived_reason_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_created_by_component_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_created_by_user_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_criticality_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_debug_mode_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_default_renewal_mode_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateDefaultRenewalModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_display_name_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_import_contacts_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateImportContactsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_import_domains_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateImportDomainsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_kind_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_labels_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_last_rate_limited_at_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateLastRateLimitedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_managed_by_content_type_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_managed_by_object_id_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_modified_by_user_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_name_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_non_field_errors_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_ote_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateOteErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_platform_dns_record_created_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_platform_service_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_provider_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_provider_id_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_provider_info_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateProviderInfoErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_provider_reference_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_reconciliation_enabled_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_sla_availability_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_sla_target_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_sla_window_days_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_slo_availability_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_slo_target_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_slo_window_days_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_target_availability_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_partial_update_tolerations_error_component import (
            ApiV1DomainsDomainRegistrarsPartialUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1DomainsDomainRegistrarsPartialUpdateAnnotationsErrorComponent
                | ApiV1DomainsDomainRegistrarsPartialUpdateApiBackoffMinutesErrorComponent
                | ApiV1DomainsDomainRegistrarsPartialUpdateApiCredentialIdErrorComponent
                | ApiV1DomainsDomainRegistrarsPartialUpdateArchivedAtErrorComponent
                | ApiV1DomainsDomainRegistrarsPartialUpdateArchivedByErrorComponent
                | ApiV1DomainsDomainRegistrarsPartialUpdateArchivedErrorComponent
                | ApiV1DomainsDomainRegistrarsPartialUpdateArchivedReasonErrorComponent
                | ApiV1DomainsDomainRegistrarsPartialUpdateCreatedByComponentErrorComponent
                | ApiV1DomainsDomainRegistrarsPartialUpdateCreatedByUserErrorComponent
                | ApiV1DomainsDomainRegistrarsPartialUpdateCriticalityErrorComponent
                | ApiV1DomainsDomainRegistrarsPartialUpdateDebugModeErrorComponent
                | ApiV1DomainsDomainRegistrarsPartialUpdateDefaultRenewalModeErrorComponent
                | ApiV1DomainsDomainRegistrarsPartialUpdateDisplayNameErrorComponent
                | ApiV1DomainsDomainRegistrarsPartialUpdateImportContactsErrorComponent
                | ApiV1DomainsDomainRegistrarsPartialUpdateImportDomainsErrorComponent
                | ApiV1DomainsDomainRegistrarsPartialUpdateKindErrorComponent
                | ApiV1DomainsDomainRegistrarsPartialUpdateLabelsErrorComponent
                | ApiV1DomainsDomainRegistrarsPartialUpdateLastRateLimitedAtErrorComponent
                | ApiV1DomainsDomainRegistrarsPartialUpdateLastReconciliationDurationSecondsErrorComponent
                | ApiV1DomainsDomainRegistrarsPartialUpdateManagedByContentTypeErrorComponent
                | ApiV1DomainsDomainRegistrarsPartialUpdateManagedByObjectIdErrorComponent
                | ApiV1DomainsDomainRegistrarsPartialUpdateModifiedByUserErrorComponent
                | ApiV1DomainsDomainRegistrarsPartialUpdateNameErrorComponent
                | ApiV1DomainsDomainRegistrarsPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1DomainsDomainRegistrarsPartialUpdateOteErrorComponent
                | ApiV1DomainsDomainRegistrarsPartialUpdatePlatformDnsRecordCreatedErrorComponent
                | ApiV1DomainsDomainRegistrarsPartialUpdatePlatformServiceErrorComponent
                | ApiV1DomainsDomainRegistrarsPartialUpdateProviderErrorComponent
                | ApiV1DomainsDomainRegistrarsPartialUpdateProviderIdErrorComponent
                | ApiV1DomainsDomainRegistrarsPartialUpdateProviderInfoErrorComponent
                | ApiV1DomainsDomainRegistrarsPartialUpdateProviderReferenceErrorComponent
                | ApiV1DomainsDomainRegistrarsPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1DomainsDomainRegistrarsPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1DomainsDomainRegistrarsPartialUpdateSlaTargetErrorComponent
                | ApiV1DomainsDomainRegistrarsPartialUpdateSlaWindowDaysErrorComponent
                | ApiV1DomainsDomainRegistrarsPartialUpdateSloAvailabilityErrorComponent
                | ApiV1DomainsDomainRegistrarsPartialUpdateSloTargetErrorComponent
                | ApiV1DomainsDomainRegistrarsPartialUpdateSloWindowDaysErrorComponent
                | ApiV1DomainsDomainRegistrarsPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1DomainsDomainRegistrarsPartialUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_0 = (
                        ApiV1DomainsDomainRegistrarsPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_1 = (
                        ApiV1DomainsDomainRegistrarsPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_2 = (
                        ApiV1DomainsDomainRegistrarsPartialUpdateApiCredentialIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_3 = (
                        ApiV1DomainsDomainRegistrarsPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_4 = (
                        ApiV1DomainsDomainRegistrarsPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_5 = (
                        ApiV1DomainsDomainRegistrarsPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_6 = (
                        ApiV1DomainsDomainRegistrarsPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_7 = (
                        ApiV1DomainsDomainRegistrarsPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_8 = (
                        ApiV1DomainsDomainRegistrarsPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_9 = (
                        ApiV1DomainsDomainRegistrarsPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_10 = (
                        ApiV1DomainsDomainRegistrarsPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_11 = ApiV1DomainsDomainRegistrarsPartialUpdateLastReconciliationDurationSecondsErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_12 = (
                        ApiV1DomainsDomainRegistrarsPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_13 = (
                        ApiV1DomainsDomainRegistrarsPartialUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_14 = (
                        ApiV1DomainsDomainRegistrarsPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_15 = (
                        ApiV1DomainsDomainRegistrarsPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_16 = (
                        ApiV1DomainsDomainRegistrarsPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_17 = (
                        ApiV1DomainsDomainRegistrarsPartialUpdateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_18 = (
                        ApiV1DomainsDomainRegistrarsPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_19 = (
                        ApiV1DomainsDomainRegistrarsPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_20 = (
                        ApiV1DomainsDomainRegistrarsPartialUpdateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_21 = (
                        ApiV1DomainsDomainRegistrarsPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_22 = (
                        ApiV1DomainsDomainRegistrarsPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_23 = (
                        ApiV1DomainsDomainRegistrarsPartialUpdateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_24 = (
                        ApiV1DomainsDomainRegistrarsPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_25 = (
                        ApiV1DomainsDomainRegistrarsPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_26 = (
                        ApiV1DomainsDomainRegistrarsPartialUpdateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_27 = (
                        ApiV1DomainsDomainRegistrarsPartialUpdatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_28 = (
                        ApiV1DomainsDomainRegistrarsPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_29 = (
                        ApiV1DomainsDomainRegistrarsPartialUpdateOteErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_30 = (
                        ApiV1DomainsDomainRegistrarsPartialUpdateDefaultRenewalModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_31 = (
                        ApiV1DomainsDomainRegistrarsPartialUpdateImportDomainsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_32 = (
                        ApiV1DomainsDomainRegistrarsPartialUpdateImportContactsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_33 = (
                        ApiV1DomainsDomainRegistrarsPartialUpdateProviderInfoErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_34 = (
                        ApiV1DomainsDomainRegistrarsPartialUpdateLastRateLimitedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_35 = (
                        ApiV1DomainsDomainRegistrarsPartialUpdateApiBackoffMinutesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_36 = (
                        ApiV1DomainsDomainRegistrarsPartialUpdateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_37 = (
                        ApiV1DomainsDomainRegistrarsPartialUpdateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_38 = (
                        ApiV1DomainsDomainRegistrarsPartialUpdateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_39 = (
                    ApiV1DomainsDomainRegistrarsPartialUpdateCreatedByUserErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_domains_domain_registrars_partial_update_error_type_39

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_domains_domain_registrars_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_domains_domain_registrars_partial_update_validation_error.additional_properties = d
        return api_v1_domains_domain_registrars_partial_update_validation_error

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
