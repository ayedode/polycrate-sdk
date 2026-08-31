from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_provider_accounts_partial_update_annotations_error_component import (
        ApiV1ProviderAccountsPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_provider_accounts_partial_update_api_backoff_minutes_error_component import (
        ApiV1ProviderAccountsPartialUpdateApiBackoffMinutesErrorComponent,
    )
    from ..models.api_v1_provider_accounts_partial_update_api_endpoint_error_component import (
        ApiV1ProviderAccountsPartialUpdateApiEndpointErrorComponent,
    )
    from ..models.api_v1_provider_accounts_partial_update_api_kind_error_component import (
        ApiV1ProviderAccountsPartialUpdateApiKindErrorComponent,
    )
    from ..models.api_v1_provider_accounts_partial_update_archived_at_error_component import (
        ApiV1ProviderAccountsPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_provider_accounts_partial_update_archived_by_error_component import (
        ApiV1ProviderAccountsPartialUpdateArchivedByErrorComponent,
    )
    from ..models.api_v1_provider_accounts_partial_update_archived_error_component import (
        ApiV1ProviderAccountsPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_provider_accounts_partial_update_archived_reason_error_component import (
        ApiV1ProviderAccountsPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_provider_accounts_partial_update_created_by_component_error_component import (
        ApiV1ProviderAccountsPartialUpdateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_provider_accounts_partial_update_created_by_user_error_component import (
        ApiV1ProviderAccountsPartialUpdateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_provider_accounts_partial_update_credential_id_error_component import (
        ApiV1ProviderAccountsPartialUpdateCredentialIdErrorComponent,
    )
    from ..models.api_v1_provider_accounts_partial_update_criticality_error_component import (
        ApiV1ProviderAccountsPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_provider_accounts_partial_update_debug_mode_error_component import (
        ApiV1ProviderAccountsPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_provider_accounts_partial_update_display_name_error_component import (
        ApiV1ProviderAccountsPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_provider_accounts_partial_update_kind_error_component import (
        ApiV1ProviderAccountsPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_provider_accounts_partial_update_labels_error_component import (
        ApiV1ProviderAccountsPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_provider_accounts_partial_update_last_rate_limited_at_error_component import (
        ApiV1ProviderAccountsPartialUpdateLastRateLimitedAtErrorComponent,
    )
    from ..models.api_v1_provider_accounts_partial_update_last_reconciliation_duration_seconds_error_component import (
        ApiV1ProviderAccountsPartialUpdateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_provider_accounts_partial_update_managed_by_content_type_error_component import (
        ApiV1ProviderAccountsPartialUpdateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_provider_accounts_partial_update_managed_by_object_id_error_component import (
        ApiV1ProviderAccountsPartialUpdateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_provider_accounts_partial_update_metadata_error_component import (
        ApiV1ProviderAccountsPartialUpdateMetadataErrorComponent,
    )
    from ..models.api_v1_provider_accounts_partial_update_modified_by_user_error_component import (
        ApiV1ProviderAccountsPartialUpdateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_provider_accounts_partial_update_name_error_component import (
        ApiV1ProviderAccountsPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_provider_accounts_partial_update_non_field_errors_error_component import (
        ApiV1ProviderAccountsPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_provider_accounts_partial_update_organization_id_error_component import (
        ApiV1ProviderAccountsPartialUpdateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_provider_accounts_partial_update_platform_dns_record_created_error_component import (
        ApiV1ProviderAccountsPartialUpdatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_provider_accounts_partial_update_platform_service_error_component import (
        ApiV1ProviderAccountsPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_provider_accounts_partial_update_provider_entity_id_error_component import (
        ApiV1ProviderAccountsPartialUpdateProviderEntityIdErrorComponent,
    )
    from ..models.api_v1_provider_accounts_partial_update_provider_error_component import (
        ApiV1ProviderAccountsPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_provider_accounts_partial_update_provider_id_error_component import (
        ApiV1ProviderAccountsPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_provider_accounts_partial_update_provider_reference_error_component import (
        ApiV1ProviderAccountsPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_provider_accounts_partial_update_reconciliation_enabled_error_component import (
        ApiV1ProviderAccountsPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_provider_accounts_partial_update_sla_availability_error_component import (
        ApiV1ProviderAccountsPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_provider_accounts_partial_update_sla_target_error_component import (
        ApiV1ProviderAccountsPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_provider_accounts_partial_update_sla_window_days_error_component import (
        ApiV1ProviderAccountsPartialUpdateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_provider_accounts_partial_update_slo_availability_error_component import (
        ApiV1ProviderAccountsPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_provider_accounts_partial_update_slo_target_error_component import (
        ApiV1ProviderAccountsPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_provider_accounts_partial_update_slo_window_days_error_component import (
        ApiV1ProviderAccountsPartialUpdateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_provider_accounts_partial_update_target_availability_error_component import (
        ApiV1ProviderAccountsPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_provider_accounts_partial_update_tolerations_error_component import (
        ApiV1ProviderAccountsPartialUpdateTolerationsErrorComponent,
    )
    from ..models.api_v1_provider_accounts_partial_update_workspace_id_error_component import (
        ApiV1ProviderAccountsPartialUpdateWorkspaceIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1ProviderAccountsPartialUpdateValidationError")


@_attrs_define
class ApiV1ProviderAccountsPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ProviderAccountsPartialUpdateAnnotationsErrorComponent |
            ApiV1ProviderAccountsPartialUpdateApiBackoffMinutesErrorComponent |
            ApiV1ProviderAccountsPartialUpdateApiEndpointErrorComponent |
            ApiV1ProviderAccountsPartialUpdateApiKindErrorComponent |
            ApiV1ProviderAccountsPartialUpdateArchivedAtErrorComponent |
            ApiV1ProviderAccountsPartialUpdateArchivedByErrorComponent |
            ApiV1ProviderAccountsPartialUpdateArchivedErrorComponent |
            ApiV1ProviderAccountsPartialUpdateArchivedReasonErrorComponent |
            ApiV1ProviderAccountsPartialUpdateCreatedByComponentErrorComponent |
            ApiV1ProviderAccountsPartialUpdateCreatedByUserErrorComponent |
            ApiV1ProviderAccountsPartialUpdateCredentialIdErrorComponent |
            ApiV1ProviderAccountsPartialUpdateCriticalityErrorComponent |
            ApiV1ProviderAccountsPartialUpdateDebugModeErrorComponent |
            ApiV1ProviderAccountsPartialUpdateDisplayNameErrorComponent |
            ApiV1ProviderAccountsPartialUpdateKindErrorComponent | ApiV1ProviderAccountsPartialUpdateLabelsErrorComponent |
            ApiV1ProviderAccountsPartialUpdateLastRateLimitedAtErrorComponent |
            ApiV1ProviderAccountsPartialUpdateLastReconciliationDurationSecondsErrorComponent |
            ApiV1ProviderAccountsPartialUpdateManagedByContentTypeErrorComponent |
            ApiV1ProviderAccountsPartialUpdateManagedByObjectIdErrorComponent |
            ApiV1ProviderAccountsPartialUpdateMetadataErrorComponent |
            ApiV1ProviderAccountsPartialUpdateModifiedByUserErrorComponent |
            ApiV1ProviderAccountsPartialUpdateNameErrorComponent |
            ApiV1ProviderAccountsPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1ProviderAccountsPartialUpdateOrganizationIdErrorComponent |
            ApiV1ProviderAccountsPartialUpdatePlatformDnsRecordCreatedErrorComponent |
            ApiV1ProviderAccountsPartialUpdatePlatformServiceErrorComponent |
            ApiV1ProviderAccountsPartialUpdateProviderEntityIdErrorComponent |
            ApiV1ProviderAccountsPartialUpdateProviderErrorComponent |
            ApiV1ProviderAccountsPartialUpdateProviderIdErrorComponent |
            ApiV1ProviderAccountsPartialUpdateProviderReferenceErrorComponent |
            ApiV1ProviderAccountsPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1ProviderAccountsPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1ProviderAccountsPartialUpdateSlaTargetErrorComponent |
            ApiV1ProviderAccountsPartialUpdateSlaWindowDaysErrorComponent |
            ApiV1ProviderAccountsPartialUpdateSloAvailabilityErrorComponent |
            ApiV1ProviderAccountsPartialUpdateSloTargetErrorComponent |
            ApiV1ProviderAccountsPartialUpdateSloWindowDaysErrorComponent |
            ApiV1ProviderAccountsPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1ProviderAccountsPartialUpdateTolerationsErrorComponent |
            ApiV1ProviderAccountsPartialUpdateWorkspaceIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ProviderAccountsPartialUpdateAnnotationsErrorComponent
        | ApiV1ProviderAccountsPartialUpdateApiBackoffMinutesErrorComponent
        | ApiV1ProviderAccountsPartialUpdateApiEndpointErrorComponent
        | ApiV1ProviderAccountsPartialUpdateApiKindErrorComponent
        | ApiV1ProviderAccountsPartialUpdateArchivedAtErrorComponent
        | ApiV1ProviderAccountsPartialUpdateArchivedByErrorComponent
        | ApiV1ProviderAccountsPartialUpdateArchivedErrorComponent
        | ApiV1ProviderAccountsPartialUpdateArchivedReasonErrorComponent
        | ApiV1ProviderAccountsPartialUpdateCreatedByComponentErrorComponent
        | ApiV1ProviderAccountsPartialUpdateCreatedByUserErrorComponent
        | ApiV1ProviderAccountsPartialUpdateCredentialIdErrorComponent
        | ApiV1ProviderAccountsPartialUpdateCriticalityErrorComponent
        | ApiV1ProviderAccountsPartialUpdateDebugModeErrorComponent
        | ApiV1ProviderAccountsPartialUpdateDisplayNameErrorComponent
        | ApiV1ProviderAccountsPartialUpdateKindErrorComponent
        | ApiV1ProviderAccountsPartialUpdateLabelsErrorComponent
        | ApiV1ProviderAccountsPartialUpdateLastRateLimitedAtErrorComponent
        | ApiV1ProviderAccountsPartialUpdateLastReconciliationDurationSecondsErrorComponent
        | ApiV1ProviderAccountsPartialUpdateManagedByContentTypeErrorComponent
        | ApiV1ProviderAccountsPartialUpdateManagedByObjectIdErrorComponent
        | ApiV1ProviderAccountsPartialUpdateMetadataErrorComponent
        | ApiV1ProviderAccountsPartialUpdateModifiedByUserErrorComponent
        | ApiV1ProviderAccountsPartialUpdateNameErrorComponent
        | ApiV1ProviderAccountsPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1ProviderAccountsPartialUpdateOrganizationIdErrorComponent
        | ApiV1ProviderAccountsPartialUpdatePlatformDnsRecordCreatedErrorComponent
        | ApiV1ProviderAccountsPartialUpdatePlatformServiceErrorComponent
        | ApiV1ProviderAccountsPartialUpdateProviderEntityIdErrorComponent
        | ApiV1ProviderAccountsPartialUpdateProviderErrorComponent
        | ApiV1ProviderAccountsPartialUpdateProviderIdErrorComponent
        | ApiV1ProviderAccountsPartialUpdateProviderReferenceErrorComponent
        | ApiV1ProviderAccountsPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1ProviderAccountsPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1ProviderAccountsPartialUpdateSlaTargetErrorComponent
        | ApiV1ProviderAccountsPartialUpdateSlaWindowDaysErrorComponent
        | ApiV1ProviderAccountsPartialUpdateSloAvailabilityErrorComponent
        | ApiV1ProviderAccountsPartialUpdateSloTargetErrorComponent
        | ApiV1ProviderAccountsPartialUpdateSloWindowDaysErrorComponent
        | ApiV1ProviderAccountsPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1ProviderAccountsPartialUpdateTolerationsErrorComponent
        | ApiV1ProviderAccountsPartialUpdateWorkspaceIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_provider_accounts_partial_update_annotations_error_component import (
            ApiV1ProviderAccountsPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_api_backoff_minutes_error_component import (
            ApiV1ProviderAccountsPartialUpdateApiBackoffMinutesErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_api_endpoint_error_component import (
            ApiV1ProviderAccountsPartialUpdateApiEndpointErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_api_kind_error_component import (
            ApiV1ProviderAccountsPartialUpdateApiKindErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_archived_at_error_component import (
            ApiV1ProviderAccountsPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_archived_by_error_component import (
            ApiV1ProviderAccountsPartialUpdateArchivedByErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_archived_error_component import (
            ApiV1ProviderAccountsPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_archived_reason_error_component import (
            ApiV1ProviderAccountsPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_created_by_component_error_component import (
            ApiV1ProviderAccountsPartialUpdateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_credential_id_error_component import (
            ApiV1ProviderAccountsPartialUpdateCredentialIdErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_criticality_error_component import (
            ApiV1ProviderAccountsPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_debug_mode_error_component import (
            ApiV1ProviderAccountsPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_display_name_error_component import (
            ApiV1ProviderAccountsPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_kind_error_component import (
            ApiV1ProviderAccountsPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_labels_error_component import (
            ApiV1ProviderAccountsPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_last_rate_limited_at_error_component import (
            ApiV1ProviderAccountsPartialUpdateLastRateLimitedAtErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1ProviderAccountsPartialUpdateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_managed_by_content_type_error_component import (
            ApiV1ProviderAccountsPartialUpdateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_managed_by_object_id_error_component import (
            ApiV1ProviderAccountsPartialUpdateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_metadata_error_component import (
            ApiV1ProviderAccountsPartialUpdateMetadataErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_modified_by_user_error_component import (
            ApiV1ProviderAccountsPartialUpdateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_name_error_component import (
            ApiV1ProviderAccountsPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_non_field_errors_error_component import (
            ApiV1ProviderAccountsPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_organization_id_error_component import (
            ApiV1ProviderAccountsPartialUpdateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_platform_dns_record_created_error_component import (
            ApiV1ProviderAccountsPartialUpdatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_platform_service_error_component import (
            ApiV1ProviderAccountsPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_provider_entity_id_error_component import (
            ApiV1ProviderAccountsPartialUpdateProviderEntityIdErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_provider_error_component import (
            ApiV1ProviderAccountsPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_provider_id_error_component import (
            ApiV1ProviderAccountsPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_provider_reference_error_component import (
            ApiV1ProviderAccountsPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_reconciliation_enabled_error_component import (
            ApiV1ProviderAccountsPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_sla_availability_error_component import (
            ApiV1ProviderAccountsPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_sla_target_error_component import (
            ApiV1ProviderAccountsPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_sla_window_days_error_component import (
            ApiV1ProviderAccountsPartialUpdateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_slo_availability_error_component import (
            ApiV1ProviderAccountsPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_slo_target_error_component import (
            ApiV1ProviderAccountsPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_slo_window_days_error_component import (
            ApiV1ProviderAccountsPartialUpdateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_target_availability_error_component import (
            ApiV1ProviderAccountsPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_tolerations_error_component import (
            ApiV1ProviderAccountsPartialUpdateTolerationsErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_workspace_id_error_component import (
            ApiV1ProviderAccountsPartialUpdateWorkspaceIdErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ProviderAccountsPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsPartialUpdateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsPartialUpdateWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsPartialUpdateProviderEntityIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsPartialUpdateCredentialIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1ProviderAccountsPartialUpdateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsPartialUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsPartialUpdateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsPartialUpdateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsPartialUpdateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsPartialUpdateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsPartialUpdatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsPartialUpdateApiKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsPartialUpdateApiEndpointErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsPartialUpdateMetadataErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsPartialUpdateLastRateLimitedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsPartialUpdateApiBackoffMinutesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsPartialUpdateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsPartialUpdateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsPartialUpdateModifiedByUserErrorComponent):
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
        from ..models.api_v1_provider_accounts_partial_update_annotations_error_component import (
            ApiV1ProviderAccountsPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_api_backoff_minutes_error_component import (
            ApiV1ProviderAccountsPartialUpdateApiBackoffMinutesErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_api_endpoint_error_component import (
            ApiV1ProviderAccountsPartialUpdateApiEndpointErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_api_kind_error_component import (
            ApiV1ProviderAccountsPartialUpdateApiKindErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_archived_at_error_component import (
            ApiV1ProviderAccountsPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_archived_by_error_component import (
            ApiV1ProviderAccountsPartialUpdateArchivedByErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_archived_error_component import (
            ApiV1ProviderAccountsPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_archived_reason_error_component import (
            ApiV1ProviderAccountsPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_created_by_component_error_component import (
            ApiV1ProviderAccountsPartialUpdateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_created_by_user_error_component import (
            ApiV1ProviderAccountsPartialUpdateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_credential_id_error_component import (
            ApiV1ProviderAccountsPartialUpdateCredentialIdErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_criticality_error_component import (
            ApiV1ProviderAccountsPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_debug_mode_error_component import (
            ApiV1ProviderAccountsPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_display_name_error_component import (
            ApiV1ProviderAccountsPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_kind_error_component import (
            ApiV1ProviderAccountsPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_labels_error_component import (
            ApiV1ProviderAccountsPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_last_rate_limited_at_error_component import (
            ApiV1ProviderAccountsPartialUpdateLastRateLimitedAtErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1ProviderAccountsPartialUpdateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_managed_by_content_type_error_component import (
            ApiV1ProviderAccountsPartialUpdateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_managed_by_object_id_error_component import (
            ApiV1ProviderAccountsPartialUpdateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_metadata_error_component import (
            ApiV1ProviderAccountsPartialUpdateMetadataErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_modified_by_user_error_component import (
            ApiV1ProviderAccountsPartialUpdateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_name_error_component import (
            ApiV1ProviderAccountsPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_non_field_errors_error_component import (
            ApiV1ProviderAccountsPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_organization_id_error_component import (
            ApiV1ProviderAccountsPartialUpdateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_platform_dns_record_created_error_component import (
            ApiV1ProviderAccountsPartialUpdatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_platform_service_error_component import (
            ApiV1ProviderAccountsPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_provider_entity_id_error_component import (
            ApiV1ProviderAccountsPartialUpdateProviderEntityIdErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_provider_error_component import (
            ApiV1ProviderAccountsPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_provider_id_error_component import (
            ApiV1ProviderAccountsPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_provider_reference_error_component import (
            ApiV1ProviderAccountsPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_reconciliation_enabled_error_component import (
            ApiV1ProviderAccountsPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_sla_availability_error_component import (
            ApiV1ProviderAccountsPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_sla_target_error_component import (
            ApiV1ProviderAccountsPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_sla_window_days_error_component import (
            ApiV1ProviderAccountsPartialUpdateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_slo_availability_error_component import (
            ApiV1ProviderAccountsPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_slo_target_error_component import (
            ApiV1ProviderAccountsPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_slo_window_days_error_component import (
            ApiV1ProviderAccountsPartialUpdateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_target_availability_error_component import (
            ApiV1ProviderAccountsPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_tolerations_error_component import (
            ApiV1ProviderAccountsPartialUpdateTolerationsErrorComponent,
        )
        from ..models.api_v1_provider_accounts_partial_update_workspace_id_error_component import (
            ApiV1ProviderAccountsPartialUpdateWorkspaceIdErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ProviderAccountsPartialUpdateAnnotationsErrorComponent
                | ApiV1ProviderAccountsPartialUpdateApiBackoffMinutesErrorComponent
                | ApiV1ProviderAccountsPartialUpdateApiEndpointErrorComponent
                | ApiV1ProviderAccountsPartialUpdateApiKindErrorComponent
                | ApiV1ProviderAccountsPartialUpdateArchivedAtErrorComponent
                | ApiV1ProviderAccountsPartialUpdateArchivedByErrorComponent
                | ApiV1ProviderAccountsPartialUpdateArchivedErrorComponent
                | ApiV1ProviderAccountsPartialUpdateArchivedReasonErrorComponent
                | ApiV1ProviderAccountsPartialUpdateCreatedByComponentErrorComponent
                | ApiV1ProviderAccountsPartialUpdateCreatedByUserErrorComponent
                | ApiV1ProviderAccountsPartialUpdateCredentialIdErrorComponent
                | ApiV1ProviderAccountsPartialUpdateCriticalityErrorComponent
                | ApiV1ProviderAccountsPartialUpdateDebugModeErrorComponent
                | ApiV1ProviderAccountsPartialUpdateDisplayNameErrorComponent
                | ApiV1ProviderAccountsPartialUpdateKindErrorComponent
                | ApiV1ProviderAccountsPartialUpdateLabelsErrorComponent
                | ApiV1ProviderAccountsPartialUpdateLastRateLimitedAtErrorComponent
                | ApiV1ProviderAccountsPartialUpdateLastReconciliationDurationSecondsErrorComponent
                | ApiV1ProviderAccountsPartialUpdateManagedByContentTypeErrorComponent
                | ApiV1ProviderAccountsPartialUpdateManagedByObjectIdErrorComponent
                | ApiV1ProviderAccountsPartialUpdateMetadataErrorComponent
                | ApiV1ProviderAccountsPartialUpdateModifiedByUserErrorComponent
                | ApiV1ProviderAccountsPartialUpdateNameErrorComponent
                | ApiV1ProviderAccountsPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1ProviderAccountsPartialUpdateOrganizationIdErrorComponent
                | ApiV1ProviderAccountsPartialUpdatePlatformDnsRecordCreatedErrorComponent
                | ApiV1ProviderAccountsPartialUpdatePlatformServiceErrorComponent
                | ApiV1ProviderAccountsPartialUpdateProviderEntityIdErrorComponent
                | ApiV1ProviderAccountsPartialUpdateProviderErrorComponent
                | ApiV1ProviderAccountsPartialUpdateProviderIdErrorComponent
                | ApiV1ProviderAccountsPartialUpdateProviderReferenceErrorComponent
                | ApiV1ProviderAccountsPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1ProviderAccountsPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1ProviderAccountsPartialUpdateSlaTargetErrorComponent
                | ApiV1ProviderAccountsPartialUpdateSlaWindowDaysErrorComponent
                | ApiV1ProviderAccountsPartialUpdateSloAvailabilityErrorComponent
                | ApiV1ProviderAccountsPartialUpdateSloTargetErrorComponent
                | ApiV1ProviderAccountsPartialUpdateSloWindowDaysErrorComponent
                | ApiV1ProviderAccountsPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1ProviderAccountsPartialUpdateTolerationsErrorComponent
                | ApiV1ProviderAccountsPartialUpdateWorkspaceIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_partial_update_error_type_0 = (
                        ApiV1ProviderAccountsPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_partial_update_error_type_1 = (
                        ApiV1ProviderAccountsPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_partial_update_error_type_2 = (
                        ApiV1ProviderAccountsPartialUpdateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_partial_update_error_type_3 = (
                        ApiV1ProviderAccountsPartialUpdateWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_partial_update_error_type_4 = (
                        ApiV1ProviderAccountsPartialUpdateProviderEntityIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_partial_update_error_type_5 = (
                        ApiV1ProviderAccountsPartialUpdateCredentialIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_partial_update_error_type_6 = (
                        ApiV1ProviderAccountsPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_partial_update_error_type_7 = (
                        ApiV1ProviderAccountsPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_partial_update_error_type_8 = (
                        ApiV1ProviderAccountsPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_partial_update_error_type_9 = (
                        ApiV1ProviderAccountsPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_partial_update_error_type_10 = (
                        ApiV1ProviderAccountsPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_partial_update_error_type_11 = (
                        ApiV1ProviderAccountsPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_partial_update_error_type_12 = (
                        ApiV1ProviderAccountsPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_partial_update_error_type_13 = (
                        ApiV1ProviderAccountsPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_partial_update_error_type_14 = (
                        ApiV1ProviderAccountsPartialUpdateLastReconciliationDurationSecondsErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_provider_accounts_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_partial_update_error_type_15 = (
                        ApiV1ProviderAccountsPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_partial_update_error_type_16 = (
                        ApiV1ProviderAccountsPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_partial_update_error_type_17 = (
                        ApiV1ProviderAccountsPartialUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_partial_update_error_type_18 = (
                        ApiV1ProviderAccountsPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_partial_update_error_type_19 = (
                        ApiV1ProviderAccountsPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_partial_update_error_type_20 = (
                        ApiV1ProviderAccountsPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_partial_update_error_type_21 = (
                        ApiV1ProviderAccountsPartialUpdateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_partial_update_error_type_22 = (
                        ApiV1ProviderAccountsPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_partial_update_error_type_23 = (
                        ApiV1ProviderAccountsPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_partial_update_error_type_24 = (
                        ApiV1ProviderAccountsPartialUpdateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_partial_update_error_type_25 = (
                        ApiV1ProviderAccountsPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_partial_update_error_type_26 = (
                        ApiV1ProviderAccountsPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_partial_update_error_type_27 = (
                        ApiV1ProviderAccountsPartialUpdateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_partial_update_error_type_28 = (
                        ApiV1ProviderAccountsPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_partial_update_error_type_29 = (
                        ApiV1ProviderAccountsPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_partial_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_partial_update_error_type_30 = (
                        ApiV1ProviderAccountsPartialUpdateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_partial_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_partial_update_error_type_31 = (
                        ApiV1ProviderAccountsPartialUpdatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_partial_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_partial_update_error_type_32 = (
                        ApiV1ProviderAccountsPartialUpdateApiKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_partial_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_partial_update_error_type_33 = (
                        ApiV1ProviderAccountsPartialUpdateApiEndpointErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_partial_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_partial_update_error_type_34 = (
                        ApiV1ProviderAccountsPartialUpdateMetadataErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_partial_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_partial_update_error_type_35 = (
                        ApiV1ProviderAccountsPartialUpdateLastRateLimitedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_partial_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_partial_update_error_type_36 = (
                        ApiV1ProviderAccountsPartialUpdateApiBackoffMinutesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_partial_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_partial_update_error_type_37 = (
                        ApiV1ProviderAccountsPartialUpdateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_partial_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_partial_update_error_type_38 = (
                        ApiV1ProviderAccountsPartialUpdateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_partial_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_partial_update_error_type_39 = (
                        ApiV1ProviderAccountsPartialUpdateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_partial_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_provider_accounts_partial_update_error_type_40 = (
                    ApiV1ProviderAccountsPartialUpdateCreatedByUserErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_provider_accounts_partial_update_error_type_40

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_provider_accounts_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_provider_accounts_partial_update_validation_error.additional_properties = d
        return api_v1_provider_accounts_partial_update_validation_error

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
