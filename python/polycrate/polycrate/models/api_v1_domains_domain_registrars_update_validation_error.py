from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_domains_domain_registrars_update_annotations_error_component import (
        ApiV1DomainsDomainRegistrarsUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_update_api_backoff_minutes_error_component import (
        ApiV1DomainsDomainRegistrarsUpdateApiBackoffMinutesErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_update_api_credential_id_error_component import (
        ApiV1DomainsDomainRegistrarsUpdateApiCredentialIdErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_update_archived_at_error_component import (
        ApiV1DomainsDomainRegistrarsUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_update_archived_by_error_component import (
        ApiV1DomainsDomainRegistrarsUpdateArchivedByErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_update_archived_error_component import (
        ApiV1DomainsDomainRegistrarsUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_update_archived_reason_error_component import (
        ApiV1DomainsDomainRegistrarsUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_update_created_by_component_error_component import (
        ApiV1DomainsDomainRegistrarsUpdateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_update_created_by_user_error_component import (
        ApiV1DomainsDomainRegistrarsUpdateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_update_criticality_error_component import (
        ApiV1DomainsDomainRegistrarsUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_update_debug_mode_error_component import (
        ApiV1DomainsDomainRegistrarsUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_update_default_renewal_mode_error_component import (
        ApiV1DomainsDomainRegistrarsUpdateDefaultRenewalModeErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_update_display_name_error_component import (
        ApiV1DomainsDomainRegistrarsUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_update_import_contacts_error_component import (
        ApiV1DomainsDomainRegistrarsUpdateImportContactsErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_update_import_domains_error_component import (
        ApiV1DomainsDomainRegistrarsUpdateImportDomainsErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_update_kind_error_component import (
        ApiV1DomainsDomainRegistrarsUpdateKindErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_update_labels_error_component import (
        ApiV1DomainsDomainRegistrarsUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_update_last_rate_limited_at_error_component import (
        ApiV1DomainsDomainRegistrarsUpdateLastRateLimitedAtErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_update_last_reconciliation_duration_seconds_error_component import (
        ApiV1DomainsDomainRegistrarsUpdateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_update_managed_by_content_type_error_component import (
        ApiV1DomainsDomainRegistrarsUpdateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_update_managed_by_object_id_error_component import (
        ApiV1DomainsDomainRegistrarsUpdateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_update_modified_by_user_error_component import (
        ApiV1DomainsDomainRegistrarsUpdateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_update_name_error_component import (
        ApiV1DomainsDomainRegistrarsUpdateNameErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_update_non_field_errors_error_component import (
        ApiV1DomainsDomainRegistrarsUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_update_ote_error_component import (
        ApiV1DomainsDomainRegistrarsUpdateOteErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_update_platform_dns_record_created_error_component import (
        ApiV1DomainsDomainRegistrarsUpdatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_update_platform_service_error_component import (
        ApiV1DomainsDomainRegistrarsUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_update_provider_error_component import (
        ApiV1DomainsDomainRegistrarsUpdateProviderErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_update_provider_id_error_component import (
        ApiV1DomainsDomainRegistrarsUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_update_provider_info_error_component import (
        ApiV1DomainsDomainRegistrarsUpdateProviderInfoErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_update_provider_reference_error_component import (
        ApiV1DomainsDomainRegistrarsUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_update_reconciliation_enabled_error_component import (
        ApiV1DomainsDomainRegistrarsUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_update_sla_availability_error_component import (
        ApiV1DomainsDomainRegistrarsUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_update_sla_target_error_component import (
        ApiV1DomainsDomainRegistrarsUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_update_sla_window_days_error_component import (
        ApiV1DomainsDomainRegistrarsUpdateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_update_slo_availability_error_component import (
        ApiV1DomainsDomainRegistrarsUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_update_slo_target_error_component import (
        ApiV1DomainsDomainRegistrarsUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_update_slo_window_days_error_component import (
        ApiV1DomainsDomainRegistrarsUpdateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_update_target_availability_error_component import (
        ApiV1DomainsDomainRegistrarsUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_domain_registrars_update_tolerations_error_component import (
        ApiV1DomainsDomainRegistrarsUpdateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1DomainsDomainRegistrarsUpdateValidationError")


@_attrs_define
class ApiV1DomainsDomainRegistrarsUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1DomainsDomainRegistrarsUpdateAnnotationsErrorComponent |
            ApiV1DomainsDomainRegistrarsUpdateApiBackoffMinutesErrorComponent |
            ApiV1DomainsDomainRegistrarsUpdateApiCredentialIdErrorComponent |
            ApiV1DomainsDomainRegistrarsUpdateArchivedAtErrorComponent |
            ApiV1DomainsDomainRegistrarsUpdateArchivedByErrorComponent |
            ApiV1DomainsDomainRegistrarsUpdateArchivedErrorComponent |
            ApiV1DomainsDomainRegistrarsUpdateArchivedReasonErrorComponent |
            ApiV1DomainsDomainRegistrarsUpdateCreatedByComponentErrorComponent |
            ApiV1DomainsDomainRegistrarsUpdateCreatedByUserErrorComponent |
            ApiV1DomainsDomainRegistrarsUpdateCriticalityErrorComponent |
            ApiV1DomainsDomainRegistrarsUpdateDebugModeErrorComponent |
            ApiV1DomainsDomainRegistrarsUpdateDefaultRenewalModeErrorComponent |
            ApiV1DomainsDomainRegistrarsUpdateDisplayNameErrorComponent |
            ApiV1DomainsDomainRegistrarsUpdateImportContactsErrorComponent |
            ApiV1DomainsDomainRegistrarsUpdateImportDomainsErrorComponent |
            ApiV1DomainsDomainRegistrarsUpdateKindErrorComponent | ApiV1DomainsDomainRegistrarsUpdateLabelsErrorComponent |
            ApiV1DomainsDomainRegistrarsUpdateLastRateLimitedAtErrorComponent |
            ApiV1DomainsDomainRegistrarsUpdateLastReconciliationDurationSecondsErrorComponent |
            ApiV1DomainsDomainRegistrarsUpdateManagedByContentTypeErrorComponent |
            ApiV1DomainsDomainRegistrarsUpdateManagedByObjectIdErrorComponent |
            ApiV1DomainsDomainRegistrarsUpdateModifiedByUserErrorComponent |
            ApiV1DomainsDomainRegistrarsUpdateNameErrorComponent |
            ApiV1DomainsDomainRegistrarsUpdateNonFieldErrorsErrorComponent |
            ApiV1DomainsDomainRegistrarsUpdateOteErrorComponent |
            ApiV1DomainsDomainRegistrarsUpdatePlatformDnsRecordCreatedErrorComponent |
            ApiV1DomainsDomainRegistrarsUpdatePlatformServiceErrorComponent |
            ApiV1DomainsDomainRegistrarsUpdateProviderErrorComponent |
            ApiV1DomainsDomainRegistrarsUpdateProviderIdErrorComponent |
            ApiV1DomainsDomainRegistrarsUpdateProviderInfoErrorComponent |
            ApiV1DomainsDomainRegistrarsUpdateProviderReferenceErrorComponent |
            ApiV1DomainsDomainRegistrarsUpdateReconciliationEnabledErrorComponent |
            ApiV1DomainsDomainRegistrarsUpdateSlaAvailabilityErrorComponent |
            ApiV1DomainsDomainRegistrarsUpdateSlaTargetErrorComponent |
            ApiV1DomainsDomainRegistrarsUpdateSlaWindowDaysErrorComponent |
            ApiV1DomainsDomainRegistrarsUpdateSloAvailabilityErrorComponent |
            ApiV1DomainsDomainRegistrarsUpdateSloTargetErrorComponent |
            ApiV1DomainsDomainRegistrarsUpdateSloWindowDaysErrorComponent |
            ApiV1DomainsDomainRegistrarsUpdateTargetAvailabilityErrorComponent |
            ApiV1DomainsDomainRegistrarsUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1DomainsDomainRegistrarsUpdateAnnotationsErrorComponent
        | ApiV1DomainsDomainRegistrarsUpdateApiBackoffMinutesErrorComponent
        | ApiV1DomainsDomainRegistrarsUpdateApiCredentialIdErrorComponent
        | ApiV1DomainsDomainRegistrarsUpdateArchivedAtErrorComponent
        | ApiV1DomainsDomainRegistrarsUpdateArchivedByErrorComponent
        | ApiV1DomainsDomainRegistrarsUpdateArchivedErrorComponent
        | ApiV1DomainsDomainRegistrarsUpdateArchivedReasonErrorComponent
        | ApiV1DomainsDomainRegistrarsUpdateCreatedByComponentErrorComponent
        | ApiV1DomainsDomainRegistrarsUpdateCreatedByUserErrorComponent
        | ApiV1DomainsDomainRegistrarsUpdateCriticalityErrorComponent
        | ApiV1DomainsDomainRegistrarsUpdateDebugModeErrorComponent
        | ApiV1DomainsDomainRegistrarsUpdateDefaultRenewalModeErrorComponent
        | ApiV1DomainsDomainRegistrarsUpdateDisplayNameErrorComponent
        | ApiV1DomainsDomainRegistrarsUpdateImportContactsErrorComponent
        | ApiV1DomainsDomainRegistrarsUpdateImportDomainsErrorComponent
        | ApiV1DomainsDomainRegistrarsUpdateKindErrorComponent
        | ApiV1DomainsDomainRegistrarsUpdateLabelsErrorComponent
        | ApiV1DomainsDomainRegistrarsUpdateLastRateLimitedAtErrorComponent
        | ApiV1DomainsDomainRegistrarsUpdateLastReconciliationDurationSecondsErrorComponent
        | ApiV1DomainsDomainRegistrarsUpdateManagedByContentTypeErrorComponent
        | ApiV1DomainsDomainRegistrarsUpdateManagedByObjectIdErrorComponent
        | ApiV1DomainsDomainRegistrarsUpdateModifiedByUserErrorComponent
        | ApiV1DomainsDomainRegistrarsUpdateNameErrorComponent
        | ApiV1DomainsDomainRegistrarsUpdateNonFieldErrorsErrorComponent
        | ApiV1DomainsDomainRegistrarsUpdateOteErrorComponent
        | ApiV1DomainsDomainRegistrarsUpdatePlatformDnsRecordCreatedErrorComponent
        | ApiV1DomainsDomainRegistrarsUpdatePlatformServiceErrorComponent
        | ApiV1DomainsDomainRegistrarsUpdateProviderErrorComponent
        | ApiV1DomainsDomainRegistrarsUpdateProviderIdErrorComponent
        | ApiV1DomainsDomainRegistrarsUpdateProviderInfoErrorComponent
        | ApiV1DomainsDomainRegistrarsUpdateProviderReferenceErrorComponent
        | ApiV1DomainsDomainRegistrarsUpdateReconciliationEnabledErrorComponent
        | ApiV1DomainsDomainRegistrarsUpdateSlaAvailabilityErrorComponent
        | ApiV1DomainsDomainRegistrarsUpdateSlaTargetErrorComponent
        | ApiV1DomainsDomainRegistrarsUpdateSlaWindowDaysErrorComponent
        | ApiV1DomainsDomainRegistrarsUpdateSloAvailabilityErrorComponent
        | ApiV1DomainsDomainRegistrarsUpdateSloTargetErrorComponent
        | ApiV1DomainsDomainRegistrarsUpdateSloWindowDaysErrorComponent
        | ApiV1DomainsDomainRegistrarsUpdateTargetAvailabilityErrorComponent
        | ApiV1DomainsDomainRegistrarsUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_domains_domain_registrars_update_annotations_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_api_backoff_minutes_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateApiBackoffMinutesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_api_credential_id_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateApiCredentialIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_archived_at_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_archived_by_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_archived_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_archived_reason_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_created_by_component_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_criticality_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_debug_mode_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_default_renewal_mode_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateDefaultRenewalModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_display_name_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_import_contacts_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateImportContactsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_import_domains_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateImportDomainsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_kind_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_labels_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_last_rate_limited_at_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateLastRateLimitedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_managed_by_content_type_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_managed_by_object_id_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_modified_by_user_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_name_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_non_field_errors_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_ote_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateOteErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_platform_dns_record_created_error_component import (
            ApiV1DomainsDomainRegistrarsUpdatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_platform_service_error_component import (
            ApiV1DomainsDomainRegistrarsUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_provider_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_provider_id_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_provider_info_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateProviderInfoErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_provider_reference_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_reconciliation_enabled_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_sla_availability_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_sla_target_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_sla_window_days_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_slo_availability_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_slo_target_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_slo_window_days_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_target_availability_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_tolerations_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsUpdateApiCredentialIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1DomainsDomainRegistrarsUpdateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsUpdateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsUpdateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsUpdateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsUpdateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsUpdatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsUpdateOteErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsUpdateDefaultRenewalModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsUpdateImportDomainsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsUpdateImportContactsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsUpdateProviderInfoErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsUpdateLastRateLimitedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsUpdateApiBackoffMinutesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsUpdateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsUpdateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainRegistrarsUpdateModifiedByUserErrorComponent):
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
        from ..models.api_v1_domains_domain_registrars_update_annotations_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_api_backoff_minutes_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateApiBackoffMinutesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_api_credential_id_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateApiCredentialIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_archived_at_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_archived_by_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_archived_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_archived_reason_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_created_by_component_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_created_by_user_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_criticality_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_debug_mode_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_default_renewal_mode_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateDefaultRenewalModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_display_name_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_import_contacts_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateImportContactsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_import_domains_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateImportDomainsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_kind_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_labels_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_last_rate_limited_at_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateLastRateLimitedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_managed_by_content_type_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_managed_by_object_id_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_modified_by_user_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_name_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_non_field_errors_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_ote_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateOteErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_platform_dns_record_created_error_component import (
            ApiV1DomainsDomainRegistrarsUpdatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_platform_service_error_component import (
            ApiV1DomainsDomainRegistrarsUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_provider_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_provider_id_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_provider_info_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateProviderInfoErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_provider_reference_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_reconciliation_enabled_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_sla_availability_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_sla_target_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_sla_window_days_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_slo_availability_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_slo_target_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_slo_window_days_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_target_availability_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domain_registrars_update_tolerations_error_component import (
            ApiV1DomainsDomainRegistrarsUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1DomainsDomainRegistrarsUpdateAnnotationsErrorComponent
                | ApiV1DomainsDomainRegistrarsUpdateApiBackoffMinutesErrorComponent
                | ApiV1DomainsDomainRegistrarsUpdateApiCredentialIdErrorComponent
                | ApiV1DomainsDomainRegistrarsUpdateArchivedAtErrorComponent
                | ApiV1DomainsDomainRegistrarsUpdateArchivedByErrorComponent
                | ApiV1DomainsDomainRegistrarsUpdateArchivedErrorComponent
                | ApiV1DomainsDomainRegistrarsUpdateArchivedReasonErrorComponent
                | ApiV1DomainsDomainRegistrarsUpdateCreatedByComponentErrorComponent
                | ApiV1DomainsDomainRegistrarsUpdateCreatedByUserErrorComponent
                | ApiV1DomainsDomainRegistrarsUpdateCriticalityErrorComponent
                | ApiV1DomainsDomainRegistrarsUpdateDebugModeErrorComponent
                | ApiV1DomainsDomainRegistrarsUpdateDefaultRenewalModeErrorComponent
                | ApiV1DomainsDomainRegistrarsUpdateDisplayNameErrorComponent
                | ApiV1DomainsDomainRegistrarsUpdateImportContactsErrorComponent
                | ApiV1DomainsDomainRegistrarsUpdateImportDomainsErrorComponent
                | ApiV1DomainsDomainRegistrarsUpdateKindErrorComponent
                | ApiV1DomainsDomainRegistrarsUpdateLabelsErrorComponent
                | ApiV1DomainsDomainRegistrarsUpdateLastRateLimitedAtErrorComponent
                | ApiV1DomainsDomainRegistrarsUpdateLastReconciliationDurationSecondsErrorComponent
                | ApiV1DomainsDomainRegistrarsUpdateManagedByContentTypeErrorComponent
                | ApiV1DomainsDomainRegistrarsUpdateManagedByObjectIdErrorComponent
                | ApiV1DomainsDomainRegistrarsUpdateModifiedByUserErrorComponent
                | ApiV1DomainsDomainRegistrarsUpdateNameErrorComponent
                | ApiV1DomainsDomainRegistrarsUpdateNonFieldErrorsErrorComponent
                | ApiV1DomainsDomainRegistrarsUpdateOteErrorComponent
                | ApiV1DomainsDomainRegistrarsUpdatePlatformDnsRecordCreatedErrorComponent
                | ApiV1DomainsDomainRegistrarsUpdatePlatformServiceErrorComponent
                | ApiV1DomainsDomainRegistrarsUpdateProviderErrorComponent
                | ApiV1DomainsDomainRegistrarsUpdateProviderIdErrorComponent
                | ApiV1DomainsDomainRegistrarsUpdateProviderInfoErrorComponent
                | ApiV1DomainsDomainRegistrarsUpdateProviderReferenceErrorComponent
                | ApiV1DomainsDomainRegistrarsUpdateReconciliationEnabledErrorComponent
                | ApiV1DomainsDomainRegistrarsUpdateSlaAvailabilityErrorComponent
                | ApiV1DomainsDomainRegistrarsUpdateSlaTargetErrorComponent
                | ApiV1DomainsDomainRegistrarsUpdateSlaWindowDaysErrorComponent
                | ApiV1DomainsDomainRegistrarsUpdateSloAvailabilityErrorComponent
                | ApiV1DomainsDomainRegistrarsUpdateSloTargetErrorComponent
                | ApiV1DomainsDomainRegistrarsUpdateSloWindowDaysErrorComponent
                | ApiV1DomainsDomainRegistrarsUpdateTargetAvailabilityErrorComponent
                | ApiV1DomainsDomainRegistrarsUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_update_error_type_0 = (
                        ApiV1DomainsDomainRegistrarsUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_update_error_type_1 = (
                        ApiV1DomainsDomainRegistrarsUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_update_error_type_2 = (
                        ApiV1DomainsDomainRegistrarsUpdateApiCredentialIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_update_error_type_3 = (
                        ApiV1DomainsDomainRegistrarsUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_update_error_type_4 = (
                        ApiV1DomainsDomainRegistrarsUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_update_error_type_5 = (
                        ApiV1DomainsDomainRegistrarsUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_update_error_type_6 = (
                        ApiV1DomainsDomainRegistrarsUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_update_error_type_7 = (
                        ApiV1DomainsDomainRegistrarsUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_update_error_type_8 = (
                        ApiV1DomainsDomainRegistrarsUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_update_error_type_9 = (
                        ApiV1DomainsDomainRegistrarsUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_update_error_type_10 = (
                        ApiV1DomainsDomainRegistrarsUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_update_error_type_11 = (
                        ApiV1DomainsDomainRegistrarsUpdateLastReconciliationDurationSecondsErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_update_error_type_12 = (
                        ApiV1DomainsDomainRegistrarsUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_update_error_type_13 = (
                        ApiV1DomainsDomainRegistrarsUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_update_error_type_14 = (
                        ApiV1DomainsDomainRegistrarsUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_update_error_type_15 = (
                        ApiV1DomainsDomainRegistrarsUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_update_error_type_16 = (
                        ApiV1DomainsDomainRegistrarsUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_update_error_type_17 = (
                        ApiV1DomainsDomainRegistrarsUpdateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_update_error_type_18 = (
                        ApiV1DomainsDomainRegistrarsUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_update_error_type_19 = (
                        ApiV1DomainsDomainRegistrarsUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_update_error_type_20 = (
                        ApiV1DomainsDomainRegistrarsUpdateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_update_error_type_21 = (
                        ApiV1DomainsDomainRegistrarsUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_update_error_type_22 = (
                        ApiV1DomainsDomainRegistrarsUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_update_error_type_23 = (
                        ApiV1DomainsDomainRegistrarsUpdateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_update_error_type_24 = (
                        ApiV1DomainsDomainRegistrarsUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_update_error_type_25 = (
                        ApiV1DomainsDomainRegistrarsUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_update_error_type_26 = (
                        ApiV1DomainsDomainRegistrarsUpdateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_update_error_type_27 = (
                        ApiV1DomainsDomainRegistrarsUpdatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_update_error_type_28 = (
                        ApiV1DomainsDomainRegistrarsUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_update_error_type_29 = (
                        ApiV1DomainsDomainRegistrarsUpdateOteErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_update_error_type_30 = (
                        ApiV1DomainsDomainRegistrarsUpdateDefaultRenewalModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_update_error_type_31 = (
                        ApiV1DomainsDomainRegistrarsUpdateImportDomainsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_update_error_type_32 = (
                        ApiV1DomainsDomainRegistrarsUpdateImportContactsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_update_error_type_33 = (
                        ApiV1DomainsDomainRegistrarsUpdateProviderInfoErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_update_error_type_34 = (
                        ApiV1DomainsDomainRegistrarsUpdateLastRateLimitedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_update_error_type_35 = (
                        ApiV1DomainsDomainRegistrarsUpdateApiBackoffMinutesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_update_error_type_36 = (
                        ApiV1DomainsDomainRegistrarsUpdateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_update_error_type_37 = (
                        ApiV1DomainsDomainRegistrarsUpdateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domain_registrars_update_error_type_38 = (
                        ApiV1DomainsDomainRegistrarsUpdateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domain_registrars_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_domains_domain_registrars_update_error_type_39 = (
                    ApiV1DomainsDomainRegistrarsUpdateCreatedByUserErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_domains_domain_registrars_update_error_type_39

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_domains_domain_registrars_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_domains_domain_registrars_update_validation_error.additional_properties = d
        return api_v1_domains_domain_registrars_update_validation_error

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
