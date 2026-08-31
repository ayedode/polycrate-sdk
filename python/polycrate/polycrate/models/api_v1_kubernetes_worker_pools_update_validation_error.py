from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_worker_pools_update_actual_availability_error_component import (
        ApiV1KubernetesWorkerPoolsUpdateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_update_annotations_error_component import (
        ApiV1KubernetesWorkerPoolsUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_update_archived_at_error_component import (
        ApiV1KubernetesWorkerPoolsUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_update_archived_error_component import (
        ApiV1KubernetesWorkerPoolsUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_update_archived_reason_error_component import (
        ApiV1KubernetesWorkerPoolsUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_update_controlplane_id_error_component import (
        ApiV1KubernetesWorkerPoolsUpdateControlplaneIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_update_criticality_error_component import (
        ApiV1KubernetesWorkerPoolsUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_update_debug_mode_error_component import (
        ApiV1KubernetesWorkerPoolsUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_update_desired_count_error_component import (
        ApiV1KubernetesWorkerPoolsUpdateDesiredCountErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_update_discovery_enabled_error_component import (
        ApiV1KubernetesWorkerPoolsUpdateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_update_display_name_error_component import (
        ApiV1KubernetesWorkerPoolsUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_update_hardening_enabled_error_component import (
        ApiV1KubernetesWorkerPoolsUpdateHardeningEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_update_image_error_component import (
        ApiV1KubernetesWorkerPoolsUpdateImageErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_update_kind_error_component import (
        ApiV1KubernetesWorkerPoolsUpdateKindErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_update_labels_error_component import (
        ApiV1KubernetesWorkerPoolsUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_update_location_error_component import (
        ApiV1KubernetesWorkerPoolsUpdateLocationErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_update_name_error_component import (
        ApiV1KubernetesWorkerPoolsUpdateNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_update_non_field_errors_error_component import (
        ApiV1KubernetesWorkerPoolsUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_update_platform_service_error_component import (
        ApiV1KubernetesWorkerPoolsUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_update_product_id_error_component import (
        ApiV1KubernetesWorkerPoolsUpdateProductIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_update_provider_account_id_error_component import (
        ApiV1KubernetesWorkerPoolsUpdateProviderAccountIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_update_provider_error_component import (
        ApiV1KubernetesWorkerPoolsUpdateProviderErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_update_provider_id_error_component import (
        ApiV1KubernetesWorkerPoolsUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_update_provider_reference_error_component import (
        ApiV1KubernetesWorkerPoolsUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_update_reconciliation_enabled_error_component import (
        ApiV1KubernetesWorkerPoolsUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_update_scope_error_component import (
        ApiV1KubernetesWorkerPoolsUpdateScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_update_sla_availability_error_component import (
        ApiV1KubernetesWorkerPoolsUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_update_sla_target_error_component import (
        ApiV1KubernetesWorkerPoolsUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_update_slo_availability_error_component import (
        ApiV1KubernetesWorkerPoolsUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_update_slo_target_error_component import (
        ApiV1KubernetesWorkerPoolsUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_update_ssh_key_credential_id_error_component import (
        ApiV1KubernetesWorkerPoolsUpdateSshKeyCredentialIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_update_target_availability_error_component import (
        ApiV1KubernetesWorkerPoolsUpdateTargetAvailabilityErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesWorkerPoolsUpdateValidationError")


@_attrs_define
class ApiV1KubernetesWorkerPoolsUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesWorkerPoolsUpdateActualAvailabilityErrorComponent |
            ApiV1KubernetesWorkerPoolsUpdateAnnotationsErrorComponent |
            ApiV1KubernetesWorkerPoolsUpdateArchivedAtErrorComponent |
            ApiV1KubernetesWorkerPoolsUpdateArchivedErrorComponent |
            ApiV1KubernetesWorkerPoolsUpdateArchivedReasonErrorComponent |
            ApiV1KubernetesWorkerPoolsUpdateControlplaneIdErrorComponent |
            ApiV1KubernetesWorkerPoolsUpdateCriticalityErrorComponent |
            ApiV1KubernetesWorkerPoolsUpdateDebugModeErrorComponent |
            ApiV1KubernetesWorkerPoolsUpdateDesiredCountErrorComponent |
            ApiV1KubernetesWorkerPoolsUpdateDiscoveryEnabledErrorComponent |
            ApiV1KubernetesWorkerPoolsUpdateDisplayNameErrorComponent |
            ApiV1KubernetesWorkerPoolsUpdateHardeningEnabledErrorComponent |
            ApiV1KubernetesWorkerPoolsUpdateImageErrorComponent | ApiV1KubernetesWorkerPoolsUpdateKindErrorComponent |
            ApiV1KubernetesWorkerPoolsUpdateLabelsErrorComponent | ApiV1KubernetesWorkerPoolsUpdateLocationErrorComponent |
            ApiV1KubernetesWorkerPoolsUpdateNameErrorComponent |
            ApiV1KubernetesWorkerPoolsUpdateNonFieldErrorsErrorComponent |
            ApiV1KubernetesWorkerPoolsUpdatePlatformServiceErrorComponent |
            ApiV1KubernetesWorkerPoolsUpdateProductIdErrorComponent |
            ApiV1KubernetesWorkerPoolsUpdateProviderAccountIdErrorComponent |
            ApiV1KubernetesWorkerPoolsUpdateProviderErrorComponent |
            ApiV1KubernetesWorkerPoolsUpdateProviderIdErrorComponent |
            ApiV1KubernetesWorkerPoolsUpdateProviderReferenceErrorComponent |
            ApiV1KubernetesWorkerPoolsUpdateReconciliationEnabledErrorComponent |
            ApiV1KubernetesWorkerPoolsUpdateScopeErrorComponent |
            ApiV1KubernetesWorkerPoolsUpdateSlaAvailabilityErrorComponent |
            ApiV1KubernetesWorkerPoolsUpdateSlaTargetErrorComponent |
            ApiV1KubernetesWorkerPoolsUpdateSloAvailabilityErrorComponent |
            ApiV1KubernetesWorkerPoolsUpdateSloTargetErrorComponent |
            ApiV1KubernetesWorkerPoolsUpdateSshKeyCredentialIdErrorComponent |
            ApiV1KubernetesWorkerPoolsUpdateTargetAvailabilityErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesWorkerPoolsUpdateActualAvailabilityErrorComponent
        | ApiV1KubernetesWorkerPoolsUpdateAnnotationsErrorComponent
        | ApiV1KubernetesWorkerPoolsUpdateArchivedAtErrorComponent
        | ApiV1KubernetesWorkerPoolsUpdateArchivedErrorComponent
        | ApiV1KubernetesWorkerPoolsUpdateArchivedReasonErrorComponent
        | ApiV1KubernetesWorkerPoolsUpdateControlplaneIdErrorComponent
        | ApiV1KubernetesWorkerPoolsUpdateCriticalityErrorComponent
        | ApiV1KubernetesWorkerPoolsUpdateDebugModeErrorComponent
        | ApiV1KubernetesWorkerPoolsUpdateDesiredCountErrorComponent
        | ApiV1KubernetesWorkerPoolsUpdateDiscoveryEnabledErrorComponent
        | ApiV1KubernetesWorkerPoolsUpdateDisplayNameErrorComponent
        | ApiV1KubernetesWorkerPoolsUpdateHardeningEnabledErrorComponent
        | ApiV1KubernetesWorkerPoolsUpdateImageErrorComponent
        | ApiV1KubernetesWorkerPoolsUpdateKindErrorComponent
        | ApiV1KubernetesWorkerPoolsUpdateLabelsErrorComponent
        | ApiV1KubernetesWorkerPoolsUpdateLocationErrorComponent
        | ApiV1KubernetesWorkerPoolsUpdateNameErrorComponent
        | ApiV1KubernetesWorkerPoolsUpdateNonFieldErrorsErrorComponent
        | ApiV1KubernetesWorkerPoolsUpdatePlatformServiceErrorComponent
        | ApiV1KubernetesWorkerPoolsUpdateProductIdErrorComponent
        | ApiV1KubernetesWorkerPoolsUpdateProviderAccountIdErrorComponent
        | ApiV1KubernetesWorkerPoolsUpdateProviderErrorComponent
        | ApiV1KubernetesWorkerPoolsUpdateProviderIdErrorComponent
        | ApiV1KubernetesWorkerPoolsUpdateProviderReferenceErrorComponent
        | ApiV1KubernetesWorkerPoolsUpdateReconciliationEnabledErrorComponent
        | ApiV1KubernetesWorkerPoolsUpdateScopeErrorComponent
        | ApiV1KubernetesWorkerPoolsUpdateSlaAvailabilityErrorComponent
        | ApiV1KubernetesWorkerPoolsUpdateSlaTargetErrorComponent
        | ApiV1KubernetesWorkerPoolsUpdateSloAvailabilityErrorComponent
        | ApiV1KubernetesWorkerPoolsUpdateSloTargetErrorComponent
        | ApiV1KubernetesWorkerPoolsUpdateSshKeyCredentialIdErrorComponent
        | ApiV1KubernetesWorkerPoolsUpdateTargetAvailabilityErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_worker_pools_update_actual_availability_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_annotations_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_archived_at_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_archived_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_archived_reason_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_controlplane_id_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateControlplaneIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_criticality_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_debug_mode_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_desired_count_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateDesiredCountErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_discovery_enabled_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_display_name_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_image_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateImageErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_kind_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_labels_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_location_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateLocationErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_name_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_non_field_errors_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_platform_service_error_component import (
            ApiV1KubernetesWorkerPoolsUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_product_id_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateProductIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_provider_account_id_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateProviderAccountIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_provider_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_provider_id_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_provider_reference_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_reconciliation_enabled_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_scope_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_sla_availability_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_sla_target_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_slo_availability_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_slo_target_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_ssh_key_credential_id_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateSshKeyCredentialIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_target_availability_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateTargetAvailabilityErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsUpdateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsUpdateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsUpdateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsUpdateControlplaneIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsUpdateProviderAccountIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsUpdateProductIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsUpdateDesiredCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsUpdateImageErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsUpdateLocationErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsUpdateSshKeyCredentialIdErrorComponent):
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
        from ..models.api_v1_kubernetes_worker_pools_update_actual_availability_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_annotations_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_archived_at_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_archived_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_archived_reason_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_controlplane_id_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateControlplaneIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_criticality_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_debug_mode_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_desired_count_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateDesiredCountErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_discovery_enabled_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_display_name_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_hardening_enabled_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateHardeningEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_image_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateImageErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_kind_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_labels_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_location_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateLocationErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_name_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_non_field_errors_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_platform_service_error_component import (
            ApiV1KubernetesWorkerPoolsUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_product_id_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateProductIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_provider_account_id_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateProviderAccountIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_provider_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_provider_id_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_provider_reference_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_reconciliation_enabled_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_scope_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_sla_availability_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_sla_target_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_slo_availability_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_slo_target_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_ssh_key_credential_id_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateSshKeyCredentialIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_update_target_availability_error_component import (
            ApiV1KubernetesWorkerPoolsUpdateTargetAvailabilityErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesWorkerPoolsUpdateActualAvailabilityErrorComponent
                | ApiV1KubernetesWorkerPoolsUpdateAnnotationsErrorComponent
                | ApiV1KubernetesWorkerPoolsUpdateArchivedAtErrorComponent
                | ApiV1KubernetesWorkerPoolsUpdateArchivedErrorComponent
                | ApiV1KubernetesWorkerPoolsUpdateArchivedReasonErrorComponent
                | ApiV1KubernetesWorkerPoolsUpdateControlplaneIdErrorComponent
                | ApiV1KubernetesWorkerPoolsUpdateCriticalityErrorComponent
                | ApiV1KubernetesWorkerPoolsUpdateDebugModeErrorComponent
                | ApiV1KubernetesWorkerPoolsUpdateDesiredCountErrorComponent
                | ApiV1KubernetesWorkerPoolsUpdateDiscoveryEnabledErrorComponent
                | ApiV1KubernetesWorkerPoolsUpdateDisplayNameErrorComponent
                | ApiV1KubernetesWorkerPoolsUpdateHardeningEnabledErrorComponent
                | ApiV1KubernetesWorkerPoolsUpdateImageErrorComponent
                | ApiV1KubernetesWorkerPoolsUpdateKindErrorComponent
                | ApiV1KubernetesWorkerPoolsUpdateLabelsErrorComponent
                | ApiV1KubernetesWorkerPoolsUpdateLocationErrorComponent
                | ApiV1KubernetesWorkerPoolsUpdateNameErrorComponent
                | ApiV1KubernetesWorkerPoolsUpdateNonFieldErrorsErrorComponent
                | ApiV1KubernetesWorkerPoolsUpdatePlatformServiceErrorComponent
                | ApiV1KubernetesWorkerPoolsUpdateProductIdErrorComponent
                | ApiV1KubernetesWorkerPoolsUpdateProviderAccountIdErrorComponent
                | ApiV1KubernetesWorkerPoolsUpdateProviderErrorComponent
                | ApiV1KubernetesWorkerPoolsUpdateProviderIdErrorComponent
                | ApiV1KubernetesWorkerPoolsUpdateProviderReferenceErrorComponent
                | ApiV1KubernetesWorkerPoolsUpdateReconciliationEnabledErrorComponent
                | ApiV1KubernetesWorkerPoolsUpdateScopeErrorComponent
                | ApiV1KubernetesWorkerPoolsUpdateSlaAvailabilityErrorComponent
                | ApiV1KubernetesWorkerPoolsUpdateSlaTargetErrorComponent
                | ApiV1KubernetesWorkerPoolsUpdateSloAvailabilityErrorComponent
                | ApiV1KubernetesWorkerPoolsUpdateSloTargetErrorComponent
                | ApiV1KubernetesWorkerPoolsUpdateSshKeyCredentialIdErrorComponent
                | ApiV1KubernetesWorkerPoolsUpdateTargetAvailabilityErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_0 = (
                        ApiV1KubernetesWorkerPoolsUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_1 = (
                        ApiV1KubernetesWorkerPoolsUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_2 = (
                        ApiV1KubernetesWorkerPoolsUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_3 = (
                        ApiV1KubernetesWorkerPoolsUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_4 = (
                        ApiV1KubernetesWorkerPoolsUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_5 = (
                        ApiV1KubernetesWorkerPoolsUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_6 = (
                        ApiV1KubernetesWorkerPoolsUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_7 = (
                        ApiV1KubernetesWorkerPoolsUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_8 = (
                        ApiV1KubernetesWorkerPoolsUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_9 = (
                        ApiV1KubernetesWorkerPoolsUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_10 = (
                        ApiV1KubernetesWorkerPoolsUpdateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_11 = (
                        ApiV1KubernetesWorkerPoolsUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_12 = (
                        ApiV1KubernetesWorkerPoolsUpdateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_13 = (
                        ApiV1KubernetesWorkerPoolsUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_14 = (
                        ApiV1KubernetesWorkerPoolsUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_15 = (
                        ApiV1KubernetesWorkerPoolsUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_16 = (
                        ApiV1KubernetesWorkerPoolsUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_17 = (
                        ApiV1KubernetesWorkerPoolsUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_18 = (
                        ApiV1KubernetesWorkerPoolsUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_19 = (
                        ApiV1KubernetesWorkerPoolsUpdateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_20 = (
                        ApiV1KubernetesWorkerPoolsUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_21 = (
                        ApiV1KubernetesWorkerPoolsUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_22 = (
                        ApiV1KubernetesWorkerPoolsUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_23 = (
                        ApiV1KubernetesWorkerPoolsUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_24 = (
                        ApiV1KubernetesWorkerPoolsUpdateControlplaneIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_25 = (
                        ApiV1KubernetesWorkerPoolsUpdateProviderAccountIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_26 = (
                        ApiV1KubernetesWorkerPoolsUpdateProductIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_27 = (
                        ApiV1KubernetesWorkerPoolsUpdateDesiredCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_28 = (
                        ApiV1KubernetesWorkerPoolsUpdateImageErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_29 = (
                        ApiV1KubernetesWorkerPoolsUpdateLocationErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_30 = (
                        ApiV1KubernetesWorkerPoolsUpdateSshKeyCredentialIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_31 = (
                    ApiV1KubernetesWorkerPoolsUpdateHardeningEnabledErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_worker_pools_update_error_type_31

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_worker_pools_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_worker_pools_update_validation_error.additional_properties = d
        return api_v1_kubernetes_worker_pools_update_validation_error

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
