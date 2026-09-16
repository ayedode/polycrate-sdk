from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_domains_domains_partial_update_admin_contact_id_error_component import (
        ApiV1DomainsDomainsPartialUpdateAdminContactIdErrorComponent,
    )
    from ..models.api_v1_domains_domains_partial_update_annotations_error_component import (
        ApiV1DomainsDomainsPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_domains_domains_partial_update_archived_at_error_component import (
        ApiV1DomainsDomainsPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_domains_domains_partial_update_archived_by_error_component import (
        ApiV1DomainsDomainsPartialUpdateArchivedByErrorComponent,
    )
    from ..models.api_v1_domains_domains_partial_update_archived_error_component import (
        ApiV1DomainsDomainsPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_domains_domains_partial_update_archived_reason_error_component import (
        ApiV1DomainsDomainsPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_domains_domains_partial_update_auth_code_credential_id_error_component import (
        ApiV1DomainsDomainsPartialUpdateAuthCodeCredentialIdErrorComponent,
    )
    from ..models.api_v1_domains_domains_partial_update_created_by_component_error_component import (
        ApiV1DomainsDomainsPartialUpdateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_domains_domains_partial_update_created_by_user_error_component import (
        ApiV1DomainsDomainsPartialUpdateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_domains_domains_partial_update_criticality_error_component import (
        ApiV1DomainsDomainsPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_domains_domains_partial_update_debug_mode_error_component import (
        ApiV1DomainsDomainsPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_domains_domains_partial_update_display_name_error_component import (
        ApiV1DomainsDomainsPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_domains_domains_partial_update_dns_zone_id_error_component import (
        ApiV1DomainsDomainsPartialUpdateDnsZoneIdErrorComponent,
    )
    from ..models.api_v1_domains_domains_partial_update_expiry_date_error_component import (
        ApiV1DomainsDomainsPartialUpdateExpiryDateErrorComponent,
    )
    from ..models.api_v1_domains_domains_partial_update_kind_error_component import (
        ApiV1DomainsDomainsPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_domains_domains_partial_update_labels_error_component import (
        ApiV1DomainsDomainsPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_domains_domains_partial_update_last_reconciliation_duration_seconds_error_component import (
        ApiV1DomainsDomainsPartialUpdateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_domains_domains_partial_update_managed_by_content_type_error_component import (
        ApiV1DomainsDomainsPartialUpdateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_domains_domains_partial_update_managed_by_object_id_error_component import (
        ApiV1DomainsDomainsPartialUpdateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_domains_domains_partial_update_modified_by_user_error_component import (
        ApiV1DomainsDomainsPartialUpdateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_domains_domains_partial_update_name_error_component import (
        ApiV1DomainsDomainsPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_domains_domains_partial_update_nameservers_error_component import (
        ApiV1DomainsDomainsPartialUpdateNameserversErrorComponent,
    )
    from ..models.api_v1_domains_domains_partial_update_non_field_errors_error_component import (
        ApiV1DomainsDomainsPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_domains_domains_partial_update_owner_contact_id_error_component import (
        ApiV1DomainsDomainsPartialUpdateOwnerContactIdErrorComponent,
    )
    from ..models.api_v1_domains_domains_partial_update_platform_dns_record_created_error_component import (
        ApiV1DomainsDomainsPartialUpdatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_domains_domains_partial_update_platform_service_error_component import (
        ApiV1DomainsDomainsPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_domains_domains_partial_update_provider_error_component import (
        ApiV1DomainsDomainsPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_domains_domains_partial_update_provider_id_error_component import (
        ApiV1DomainsDomainsPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_domains_domains_partial_update_provider_reference_error_component import (
        ApiV1DomainsDomainsPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_domains_domains_partial_update_provider_status_error_component import (
        ApiV1DomainsDomainsPartialUpdateProviderStatusErrorComponent,
    )
    from ..models.api_v1_domains_domains_partial_update_reconciliation_enabled_error_component import (
        ApiV1DomainsDomainsPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_domains_domains_partial_update_registrar_domain_id_error_component import (
        ApiV1DomainsDomainsPartialUpdateRegistrarDomainIdErrorComponent,
    )
    from ..models.api_v1_domains_domains_partial_update_registrar_id_error_component import (
        ApiV1DomainsDomainsPartialUpdateRegistrarIdErrorComponent,
    )
    from ..models.api_v1_domains_domains_partial_update_registrar_metadata_error_component import (
        ApiV1DomainsDomainsPartialUpdateRegistrarMetadataErrorComponent,
    )
    from ..models.api_v1_domains_domains_partial_update_renewal_mode_error_component import (
        ApiV1DomainsDomainsPartialUpdateRenewalModeErrorComponent,
    )
    from ..models.api_v1_domains_domains_partial_update_sla_availability_error_component import (
        ApiV1DomainsDomainsPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_domains_partial_update_sla_target_error_component import (
        ApiV1DomainsDomainsPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_domains_domains_partial_update_sla_window_days_error_component import (
        ApiV1DomainsDomainsPartialUpdateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_domains_domains_partial_update_slo_availability_error_component import (
        ApiV1DomainsDomainsPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_domains_partial_update_slo_target_error_component import (
        ApiV1DomainsDomainsPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_domains_domains_partial_update_slo_window_days_error_component import (
        ApiV1DomainsDomainsPartialUpdateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_domains_domains_partial_update_target_availability_error_component import (
        ApiV1DomainsDomainsPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_domains_partial_update_tech_contact_id_error_component import (
        ApiV1DomainsDomainsPartialUpdateTechContactIdErrorComponent,
    )
    from ..models.api_v1_domains_domains_partial_update_tolerations_error_component import (
        ApiV1DomainsDomainsPartialUpdateTolerationsErrorComponent,
    )
    from ..models.api_v1_domains_domains_partial_update_transfer_lock_error_component import (
        ApiV1DomainsDomainsPartialUpdateTransferLockErrorComponent,
    )
    from ..models.api_v1_domains_domains_partial_update_use_platform_dns_error_component import (
        ApiV1DomainsDomainsPartialUpdateUsePlatformDnsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1DomainsDomainsPartialUpdateValidationError")


@_attrs_define
class ApiV1DomainsDomainsPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1DomainsDomainsPartialUpdateAdminContactIdErrorComponent |
            ApiV1DomainsDomainsPartialUpdateAnnotationsErrorComponent |
            ApiV1DomainsDomainsPartialUpdateArchivedAtErrorComponent |
            ApiV1DomainsDomainsPartialUpdateArchivedByErrorComponent |
            ApiV1DomainsDomainsPartialUpdateArchivedErrorComponent |
            ApiV1DomainsDomainsPartialUpdateArchivedReasonErrorComponent |
            ApiV1DomainsDomainsPartialUpdateAuthCodeCredentialIdErrorComponent |
            ApiV1DomainsDomainsPartialUpdateCreatedByComponentErrorComponent |
            ApiV1DomainsDomainsPartialUpdateCreatedByUserErrorComponent |
            ApiV1DomainsDomainsPartialUpdateCriticalityErrorComponent |
            ApiV1DomainsDomainsPartialUpdateDebugModeErrorComponent |
            ApiV1DomainsDomainsPartialUpdateDisplayNameErrorComponent |
            ApiV1DomainsDomainsPartialUpdateDnsZoneIdErrorComponent |
            ApiV1DomainsDomainsPartialUpdateExpiryDateErrorComponent | ApiV1DomainsDomainsPartialUpdateKindErrorComponent |
            ApiV1DomainsDomainsPartialUpdateLabelsErrorComponent |
            ApiV1DomainsDomainsPartialUpdateLastReconciliationDurationSecondsErrorComponent |
            ApiV1DomainsDomainsPartialUpdateManagedByContentTypeErrorComponent |
            ApiV1DomainsDomainsPartialUpdateManagedByObjectIdErrorComponent |
            ApiV1DomainsDomainsPartialUpdateModifiedByUserErrorComponent |
            ApiV1DomainsDomainsPartialUpdateNameErrorComponent | ApiV1DomainsDomainsPartialUpdateNameserversErrorComponent |
            ApiV1DomainsDomainsPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1DomainsDomainsPartialUpdateOwnerContactIdErrorComponent |
            ApiV1DomainsDomainsPartialUpdatePlatformDnsRecordCreatedErrorComponent |
            ApiV1DomainsDomainsPartialUpdatePlatformServiceErrorComponent |
            ApiV1DomainsDomainsPartialUpdateProviderErrorComponent |
            ApiV1DomainsDomainsPartialUpdateProviderIdErrorComponent |
            ApiV1DomainsDomainsPartialUpdateProviderReferenceErrorComponent |
            ApiV1DomainsDomainsPartialUpdateProviderStatusErrorComponent |
            ApiV1DomainsDomainsPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1DomainsDomainsPartialUpdateRegistrarDomainIdErrorComponent |
            ApiV1DomainsDomainsPartialUpdateRegistrarIdErrorComponent |
            ApiV1DomainsDomainsPartialUpdateRegistrarMetadataErrorComponent |
            ApiV1DomainsDomainsPartialUpdateRenewalModeErrorComponent |
            ApiV1DomainsDomainsPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1DomainsDomainsPartialUpdateSlaTargetErrorComponent |
            ApiV1DomainsDomainsPartialUpdateSlaWindowDaysErrorComponent |
            ApiV1DomainsDomainsPartialUpdateSloAvailabilityErrorComponent |
            ApiV1DomainsDomainsPartialUpdateSloTargetErrorComponent |
            ApiV1DomainsDomainsPartialUpdateSloWindowDaysErrorComponent |
            ApiV1DomainsDomainsPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1DomainsDomainsPartialUpdateTechContactIdErrorComponent |
            ApiV1DomainsDomainsPartialUpdateTolerationsErrorComponent |
            ApiV1DomainsDomainsPartialUpdateTransferLockErrorComponent |
            ApiV1DomainsDomainsPartialUpdateUsePlatformDnsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1DomainsDomainsPartialUpdateAdminContactIdErrorComponent
        | ApiV1DomainsDomainsPartialUpdateAnnotationsErrorComponent
        | ApiV1DomainsDomainsPartialUpdateArchivedAtErrorComponent
        | ApiV1DomainsDomainsPartialUpdateArchivedByErrorComponent
        | ApiV1DomainsDomainsPartialUpdateArchivedErrorComponent
        | ApiV1DomainsDomainsPartialUpdateArchivedReasonErrorComponent
        | ApiV1DomainsDomainsPartialUpdateAuthCodeCredentialIdErrorComponent
        | ApiV1DomainsDomainsPartialUpdateCreatedByComponentErrorComponent
        | ApiV1DomainsDomainsPartialUpdateCreatedByUserErrorComponent
        | ApiV1DomainsDomainsPartialUpdateCriticalityErrorComponent
        | ApiV1DomainsDomainsPartialUpdateDebugModeErrorComponent
        | ApiV1DomainsDomainsPartialUpdateDisplayNameErrorComponent
        | ApiV1DomainsDomainsPartialUpdateDnsZoneIdErrorComponent
        | ApiV1DomainsDomainsPartialUpdateExpiryDateErrorComponent
        | ApiV1DomainsDomainsPartialUpdateKindErrorComponent
        | ApiV1DomainsDomainsPartialUpdateLabelsErrorComponent
        | ApiV1DomainsDomainsPartialUpdateLastReconciliationDurationSecondsErrorComponent
        | ApiV1DomainsDomainsPartialUpdateManagedByContentTypeErrorComponent
        | ApiV1DomainsDomainsPartialUpdateManagedByObjectIdErrorComponent
        | ApiV1DomainsDomainsPartialUpdateModifiedByUserErrorComponent
        | ApiV1DomainsDomainsPartialUpdateNameErrorComponent
        | ApiV1DomainsDomainsPartialUpdateNameserversErrorComponent
        | ApiV1DomainsDomainsPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1DomainsDomainsPartialUpdateOwnerContactIdErrorComponent
        | ApiV1DomainsDomainsPartialUpdatePlatformDnsRecordCreatedErrorComponent
        | ApiV1DomainsDomainsPartialUpdatePlatformServiceErrorComponent
        | ApiV1DomainsDomainsPartialUpdateProviderErrorComponent
        | ApiV1DomainsDomainsPartialUpdateProviderIdErrorComponent
        | ApiV1DomainsDomainsPartialUpdateProviderReferenceErrorComponent
        | ApiV1DomainsDomainsPartialUpdateProviderStatusErrorComponent
        | ApiV1DomainsDomainsPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1DomainsDomainsPartialUpdateRegistrarDomainIdErrorComponent
        | ApiV1DomainsDomainsPartialUpdateRegistrarIdErrorComponent
        | ApiV1DomainsDomainsPartialUpdateRegistrarMetadataErrorComponent
        | ApiV1DomainsDomainsPartialUpdateRenewalModeErrorComponent
        | ApiV1DomainsDomainsPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1DomainsDomainsPartialUpdateSlaTargetErrorComponent
        | ApiV1DomainsDomainsPartialUpdateSlaWindowDaysErrorComponent
        | ApiV1DomainsDomainsPartialUpdateSloAvailabilityErrorComponent
        | ApiV1DomainsDomainsPartialUpdateSloTargetErrorComponent
        | ApiV1DomainsDomainsPartialUpdateSloWindowDaysErrorComponent
        | ApiV1DomainsDomainsPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1DomainsDomainsPartialUpdateTechContactIdErrorComponent
        | ApiV1DomainsDomainsPartialUpdateTolerationsErrorComponent
        | ApiV1DomainsDomainsPartialUpdateTransferLockErrorComponent
        | ApiV1DomainsDomainsPartialUpdateUsePlatformDnsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_domains_domains_partial_update_admin_contact_id_error_component import (
            ApiV1DomainsDomainsPartialUpdateAdminContactIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_annotations_error_component import (
            ApiV1DomainsDomainsPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_archived_at_error_component import (
            ApiV1DomainsDomainsPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_archived_by_error_component import (
            ApiV1DomainsDomainsPartialUpdateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_archived_error_component import (
            ApiV1DomainsDomainsPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_archived_reason_error_component import (
            ApiV1DomainsDomainsPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_auth_code_credential_id_error_component import (
            ApiV1DomainsDomainsPartialUpdateAuthCodeCredentialIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_created_by_component_error_component import (
            ApiV1DomainsDomainsPartialUpdateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_criticality_error_component import (
            ApiV1DomainsDomainsPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_debug_mode_error_component import (
            ApiV1DomainsDomainsPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_display_name_error_component import (
            ApiV1DomainsDomainsPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_dns_zone_id_error_component import (
            ApiV1DomainsDomainsPartialUpdateDnsZoneIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_expiry_date_error_component import (
            ApiV1DomainsDomainsPartialUpdateExpiryDateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_kind_error_component import (
            ApiV1DomainsDomainsPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_labels_error_component import (
            ApiV1DomainsDomainsPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1DomainsDomainsPartialUpdateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_managed_by_content_type_error_component import (
            ApiV1DomainsDomainsPartialUpdateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_managed_by_object_id_error_component import (
            ApiV1DomainsDomainsPartialUpdateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_modified_by_user_error_component import (
            ApiV1DomainsDomainsPartialUpdateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_name_error_component import (
            ApiV1DomainsDomainsPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_nameservers_error_component import (
            ApiV1DomainsDomainsPartialUpdateNameserversErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_non_field_errors_error_component import (
            ApiV1DomainsDomainsPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_owner_contact_id_error_component import (
            ApiV1DomainsDomainsPartialUpdateOwnerContactIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_platform_dns_record_created_error_component import (
            ApiV1DomainsDomainsPartialUpdatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_platform_service_error_component import (
            ApiV1DomainsDomainsPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_provider_error_component import (
            ApiV1DomainsDomainsPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_provider_id_error_component import (
            ApiV1DomainsDomainsPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_provider_reference_error_component import (
            ApiV1DomainsDomainsPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_provider_status_error_component import (
            ApiV1DomainsDomainsPartialUpdateProviderStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_reconciliation_enabled_error_component import (
            ApiV1DomainsDomainsPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_registrar_domain_id_error_component import (
            ApiV1DomainsDomainsPartialUpdateRegistrarDomainIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_registrar_id_error_component import (
            ApiV1DomainsDomainsPartialUpdateRegistrarIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_registrar_metadata_error_component import (
            ApiV1DomainsDomainsPartialUpdateRegistrarMetadataErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_renewal_mode_error_component import (
            ApiV1DomainsDomainsPartialUpdateRenewalModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_sla_availability_error_component import (
            ApiV1DomainsDomainsPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_sla_target_error_component import (
            ApiV1DomainsDomainsPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_sla_window_days_error_component import (
            ApiV1DomainsDomainsPartialUpdateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_slo_availability_error_component import (
            ApiV1DomainsDomainsPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_slo_target_error_component import (
            ApiV1DomainsDomainsPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_slo_window_days_error_component import (
            ApiV1DomainsDomainsPartialUpdateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_target_availability_error_component import (
            ApiV1DomainsDomainsPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_tech_contact_id_error_component import (
            ApiV1DomainsDomainsPartialUpdateTechContactIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_tolerations_error_component import (
            ApiV1DomainsDomainsPartialUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_transfer_lock_error_component import (
            ApiV1DomainsDomainsPartialUpdateTransferLockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_use_platform_dns_error_component import (
            ApiV1DomainsDomainsPartialUpdateUsePlatformDnsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1DomainsDomainsPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsPartialUpdateRegistrarIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsPartialUpdateDnsZoneIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsPartialUpdateUsePlatformDnsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsPartialUpdateOwnerContactIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsPartialUpdateAdminContactIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsPartialUpdateTechContactIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsPartialUpdateAuthCodeCredentialIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1DomainsDomainsPartialUpdateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsPartialUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsPartialUpdateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsPartialUpdateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsPartialUpdateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsPartialUpdateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsPartialUpdatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsPartialUpdateNameserversErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsPartialUpdateRenewalModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsPartialUpdateTransferLockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsPartialUpdateRegistrarDomainIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsPartialUpdateProviderStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsPartialUpdateExpiryDateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsPartialUpdateRegistrarMetadataErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsPartialUpdateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsPartialUpdateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsPartialUpdateModifiedByUserErrorComponent):
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
        from ..models.api_v1_domains_domains_partial_update_admin_contact_id_error_component import (
            ApiV1DomainsDomainsPartialUpdateAdminContactIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_annotations_error_component import (
            ApiV1DomainsDomainsPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_archived_at_error_component import (
            ApiV1DomainsDomainsPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_archived_by_error_component import (
            ApiV1DomainsDomainsPartialUpdateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_archived_error_component import (
            ApiV1DomainsDomainsPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_archived_reason_error_component import (
            ApiV1DomainsDomainsPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_auth_code_credential_id_error_component import (
            ApiV1DomainsDomainsPartialUpdateAuthCodeCredentialIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_created_by_component_error_component import (
            ApiV1DomainsDomainsPartialUpdateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_created_by_user_error_component import (
            ApiV1DomainsDomainsPartialUpdateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_criticality_error_component import (
            ApiV1DomainsDomainsPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_debug_mode_error_component import (
            ApiV1DomainsDomainsPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_display_name_error_component import (
            ApiV1DomainsDomainsPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_dns_zone_id_error_component import (
            ApiV1DomainsDomainsPartialUpdateDnsZoneIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_expiry_date_error_component import (
            ApiV1DomainsDomainsPartialUpdateExpiryDateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_kind_error_component import (
            ApiV1DomainsDomainsPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_labels_error_component import (
            ApiV1DomainsDomainsPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1DomainsDomainsPartialUpdateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_managed_by_content_type_error_component import (
            ApiV1DomainsDomainsPartialUpdateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_managed_by_object_id_error_component import (
            ApiV1DomainsDomainsPartialUpdateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_modified_by_user_error_component import (
            ApiV1DomainsDomainsPartialUpdateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_name_error_component import (
            ApiV1DomainsDomainsPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_nameservers_error_component import (
            ApiV1DomainsDomainsPartialUpdateNameserversErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_non_field_errors_error_component import (
            ApiV1DomainsDomainsPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_owner_contact_id_error_component import (
            ApiV1DomainsDomainsPartialUpdateOwnerContactIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_platform_dns_record_created_error_component import (
            ApiV1DomainsDomainsPartialUpdatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_platform_service_error_component import (
            ApiV1DomainsDomainsPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_provider_error_component import (
            ApiV1DomainsDomainsPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_provider_id_error_component import (
            ApiV1DomainsDomainsPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_provider_reference_error_component import (
            ApiV1DomainsDomainsPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_provider_status_error_component import (
            ApiV1DomainsDomainsPartialUpdateProviderStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_reconciliation_enabled_error_component import (
            ApiV1DomainsDomainsPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_registrar_domain_id_error_component import (
            ApiV1DomainsDomainsPartialUpdateRegistrarDomainIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_registrar_id_error_component import (
            ApiV1DomainsDomainsPartialUpdateRegistrarIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_registrar_metadata_error_component import (
            ApiV1DomainsDomainsPartialUpdateRegistrarMetadataErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_renewal_mode_error_component import (
            ApiV1DomainsDomainsPartialUpdateRenewalModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_sla_availability_error_component import (
            ApiV1DomainsDomainsPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_sla_target_error_component import (
            ApiV1DomainsDomainsPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_sla_window_days_error_component import (
            ApiV1DomainsDomainsPartialUpdateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_slo_availability_error_component import (
            ApiV1DomainsDomainsPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_slo_target_error_component import (
            ApiV1DomainsDomainsPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_slo_window_days_error_component import (
            ApiV1DomainsDomainsPartialUpdateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_target_availability_error_component import (
            ApiV1DomainsDomainsPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_tech_contact_id_error_component import (
            ApiV1DomainsDomainsPartialUpdateTechContactIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_tolerations_error_component import (
            ApiV1DomainsDomainsPartialUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_transfer_lock_error_component import (
            ApiV1DomainsDomainsPartialUpdateTransferLockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_partial_update_use_platform_dns_error_component import (
            ApiV1DomainsDomainsPartialUpdateUsePlatformDnsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1DomainsDomainsPartialUpdateAdminContactIdErrorComponent
                | ApiV1DomainsDomainsPartialUpdateAnnotationsErrorComponent
                | ApiV1DomainsDomainsPartialUpdateArchivedAtErrorComponent
                | ApiV1DomainsDomainsPartialUpdateArchivedByErrorComponent
                | ApiV1DomainsDomainsPartialUpdateArchivedErrorComponent
                | ApiV1DomainsDomainsPartialUpdateArchivedReasonErrorComponent
                | ApiV1DomainsDomainsPartialUpdateAuthCodeCredentialIdErrorComponent
                | ApiV1DomainsDomainsPartialUpdateCreatedByComponentErrorComponent
                | ApiV1DomainsDomainsPartialUpdateCreatedByUserErrorComponent
                | ApiV1DomainsDomainsPartialUpdateCriticalityErrorComponent
                | ApiV1DomainsDomainsPartialUpdateDebugModeErrorComponent
                | ApiV1DomainsDomainsPartialUpdateDisplayNameErrorComponent
                | ApiV1DomainsDomainsPartialUpdateDnsZoneIdErrorComponent
                | ApiV1DomainsDomainsPartialUpdateExpiryDateErrorComponent
                | ApiV1DomainsDomainsPartialUpdateKindErrorComponent
                | ApiV1DomainsDomainsPartialUpdateLabelsErrorComponent
                | ApiV1DomainsDomainsPartialUpdateLastReconciliationDurationSecondsErrorComponent
                | ApiV1DomainsDomainsPartialUpdateManagedByContentTypeErrorComponent
                | ApiV1DomainsDomainsPartialUpdateManagedByObjectIdErrorComponent
                | ApiV1DomainsDomainsPartialUpdateModifiedByUserErrorComponent
                | ApiV1DomainsDomainsPartialUpdateNameErrorComponent
                | ApiV1DomainsDomainsPartialUpdateNameserversErrorComponent
                | ApiV1DomainsDomainsPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1DomainsDomainsPartialUpdateOwnerContactIdErrorComponent
                | ApiV1DomainsDomainsPartialUpdatePlatformDnsRecordCreatedErrorComponent
                | ApiV1DomainsDomainsPartialUpdatePlatformServiceErrorComponent
                | ApiV1DomainsDomainsPartialUpdateProviderErrorComponent
                | ApiV1DomainsDomainsPartialUpdateProviderIdErrorComponent
                | ApiV1DomainsDomainsPartialUpdateProviderReferenceErrorComponent
                | ApiV1DomainsDomainsPartialUpdateProviderStatusErrorComponent
                | ApiV1DomainsDomainsPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1DomainsDomainsPartialUpdateRegistrarDomainIdErrorComponent
                | ApiV1DomainsDomainsPartialUpdateRegistrarIdErrorComponent
                | ApiV1DomainsDomainsPartialUpdateRegistrarMetadataErrorComponent
                | ApiV1DomainsDomainsPartialUpdateRenewalModeErrorComponent
                | ApiV1DomainsDomainsPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1DomainsDomainsPartialUpdateSlaTargetErrorComponent
                | ApiV1DomainsDomainsPartialUpdateSlaWindowDaysErrorComponent
                | ApiV1DomainsDomainsPartialUpdateSloAvailabilityErrorComponent
                | ApiV1DomainsDomainsPartialUpdateSloTargetErrorComponent
                | ApiV1DomainsDomainsPartialUpdateSloWindowDaysErrorComponent
                | ApiV1DomainsDomainsPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1DomainsDomainsPartialUpdateTechContactIdErrorComponent
                | ApiV1DomainsDomainsPartialUpdateTolerationsErrorComponent
                | ApiV1DomainsDomainsPartialUpdateTransferLockErrorComponent
                | ApiV1DomainsDomainsPartialUpdateUsePlatformDnsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_partial_update_error_type_0 = (
                        ApiV1DomainsDomainsPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_partial_update_error_type_1 = (
                        ApiV1DomainsDomainsPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_partial_update_error_type_2 = (
                        ApiV1DomainsDomainsPartialUpdateRegistrarIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_partial_update_error_type_3 = (
                        ApiV1DomainsDomainsPartialUpdateDnsZoneIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_partial_update_error_type_4 = (
                        ApiV1DomainsDomainsPartialUpdateUsePlatformDnsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_partial_update_error_type_5 = (
                        ApiV1DomainsDomainsPartialUpdateOwnerContactIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_partial_update_error_type_6 = (
                        ApiV1DomainsDomainsPartialUpdateAdminContactIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_partial_update_error_type_7 = (
                        ApiV1DomainsDomainsPartialUpdateTechContactIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_partial_update_error_type_8 = (
                        ApiV1DomainsDomainsPartialUpdateAuthCodeCredentialIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_partial_update_error_type_9 = (
                        ApiV1DomainsDomainsPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_partial_update_error_type_10 = (
                        ApiV1DomainsDomainsPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_partial_update_error_type_11 = (
                        ApiV1DomainsDomainsPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_partial_update_error_type_12 = (
                        ApiV1DomainsDomainsPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_partial_update_error_type_13 = (
                        ApiV1DomainsDomainsPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_partial_update_error_type_14 = (
                        ApiV1DomainsDomainsPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_partial_update_error_type_15 = (
                        ApiV1DomainsDomainsPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_partial_update_error_type_16 = (
                        ApiV1DomainsDomainsPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_partial_update_error_type_17 = (
                        ApiV1DomainsDomainsPartialUpdateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_partial_update_error_type_18 = (
                        ApiV1DomainsDomainsPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_partial_update_error_type_19 = (
                        ApiV1DomainsDomainsPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_partial_update_error_type_20 = (
                        ApiV1DomainsDomainsPartialUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_partial_update_error_type_21 = (
                        ApiV1DomainsDomainsPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_partial_update_error_type_22 = (
                        ApiV1DomainsDomainsPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_partial_update_error_type_23 = (
                        ApiV1DomainsDomainsPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_partial_update_error_type_24 = (
                        ApiV1DomainsDomainsPartialUpdateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_partial_update_error_type_25 = (
                        ApiV1DomainsDomainsPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_partial_update_error_type_26 = (
                        ApiV1DomainsDomainsPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_partial_update_error_type_27 = (
                        ApiV1DomainsDomainsPartialUpdateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_partial_update_error_type_28 = (
                        ApiV1DomainsDomainsPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_partial_update_error_type_29 = (
                        ApiV1DomainsDomainsPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_partial_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_partial_update_error_type_30 = (
                        ApiV1DomainsDomainsPartialUpdateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_partial_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_partial_update_error_type_31 = (
                        ApiV1DomainsDomainsPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_partial_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_partial_update_error_type_32 = (
                        ApiV1DomainsDomainsPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_partial_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_partial_update_error_type_33 = (
                        ApiV1DomainsDomainsPartialUpdateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_partial_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_partial_update_error_type_34 = (
                        ApiV1DomainsDomainsPartialUpdatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_partial_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_partial_update_error_type_35 = (
                        ApiV1DomainsDomainsPartialUpdateNameserversErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_partial_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_partial_update_error_type_36 = (
                        ApiV1DomainsDomainsPartialUpdateRenewalModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_partial_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_partial_update_error_type_37 = (
                        ApiV1DomainsDomainsPartialUpdateTransferLockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_partial_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_partial_update_error_type_38 = (
                        ApiV1DomainsDomainsPartialUpdateRegistrarDomainIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_partial_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_partial_update_error_type_39 = (
                        ApiV1DomainsDomainsPartialUpdateProviderStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_partial_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_partial_update_error_type_40 = (
                        ApiV1DomainsDomainsPartialUpdateExpiryDateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_partial_update_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_partial_update_error_type_41 = (
                        ApiV1DomainsDomainsPartialUpdateRegistrarMetadataErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_partial_update_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_partial_update_error_type_42 = (
                        ApiV1DomainsDomainsPartialUpdateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_partial_update_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_partial_update_error_type_43 = (
                        ApiV1DomainsDomainsPartialUpdateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_partial_update_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_partial_update_error_type_44 = (
                        ApiV1DomainsDomainsPartialUpdateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_partial_update_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_domains_domains_partial_update_error_type_45 = (
                    ApiV1DomainsDomainsPartialUpdateCreatedByUserErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_domains_domains_partial_update_error_type_45

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_domains_domains_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_domains_domains_partial_update_validation_error.additional_properties = d
        return api_v1_domains_domains_partial_update_validation_error

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
