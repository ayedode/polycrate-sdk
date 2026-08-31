from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_actual_availability_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsUpdateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_addon_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsUpdateAddonErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_annotations_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_archived_at_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_archived_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_archived_reason_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_block_config_template_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsUpdateBlockConfigTemplateErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_block_name_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsUpdateBlockNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_criticality_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_debug_mode_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_discovery_enabled_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsUpdateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_display_name_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_k8s_cluster_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsUpdateK8SClusterErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_kind_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsUpdateKindErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_labels_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_name_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsUpdateNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_non_field_errors_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_order_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsUpdateOrderErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_platform_service_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_provider_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsUpdateProviderErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_provider_id_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_provider_reference_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_reconciliation_enabled_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_scope_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsUpdateScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_sla_availability_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_sla_target_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_slo_availability_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_slo_target_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_target_availability_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_version_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsUpdateVersionErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesClusterAddonSubscriptionsUpdateValidationError")


@_attrs_define
class ApiV1KubernetesClusterAddonSubscriptionsUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesClusterAddonSubscriptionsUpdateActualAvailabilityErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsUpdateAddonErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsUpdateAnnotationsErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsUpdateArchivedAtErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsUpdateArchivedErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsUpdateArchivedReasonErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsUpdateBlockConfigTemplateErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsUpdateBlockNameErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsUpdateCriticalityErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsUpdateDebugModeErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsUpdateDiscoveryEnabledErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsUpdateDisplayNameErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsUpdateK8SClusterErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsUpdateKindErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsUpdateLabelsErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsUpdateNameErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsUpdateNonFieldErrorsErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsUpdateOrderErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsUpdatePlatformServiceErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsUpdateProviderErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsUpdateProviderIdErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsUpdateProviderReferenceErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsUpdateReconciliationEnabledErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsUpdateScopeErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsUpdateSlaAvailabilityErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsUpdateSlaTargetErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsUpdateSloAvailabilityErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsUpdateSloTargetErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsUpdateTargetAvailabilityErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsUpdateVersionErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesClusterAddonSubscriptionsUpdateActualAvailabilityErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsUpdateAddonErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsUpdateAnnotationsErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsUpdateArchivedAtErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsUpdateArchivedErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsUpdateArchivedReasonErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsUpdateBlockConfigTemplateErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsUpdateBlockNameErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsUpdateCriticalityErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsUpdateDebugModeErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsUpdateDiscoveryEnabledErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsUpdateDisplayNameErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsUpdateK8SClusterErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsUpdateKindErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsUpdateLabelsErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsUpdateNameErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsUpdateNonFieldErrorsErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsUpdateOrderErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsUpdatePlatformServiceErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsUpdateProviderErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsUpdateProviderIdErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsUpdateProviderReferenceErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsUpdateReconciliationEnabledErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsUpdateScopeErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsUpdateSlaAvailabilityErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsUpdateSlaTargetErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsUpdateSloAvailabilityErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsUpdateSloTargetErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsUpdateTargetAvailabilityErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsUpdateVersionErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_actual_availability_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_addon_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateAddonErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_annotations_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_archived_at_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_archived_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_archived_reason_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_block_config_template_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateBlockConfigTemplateErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_block_name_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateBlockNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_criticality_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_debug_mode_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_discovery_enabled_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_display_name_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_k8s_cluster_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateK8SClusterErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_kind_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_labels_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_name_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_non_field_errors_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_platform_service_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_provider_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_provider_id_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_provider_reference_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_reconciliation_enabled_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_scope_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_sla_availability_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_sla_target_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_slo_availability_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_slo_target_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_target_availability_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_version_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateVersionErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsUpdateProviderReferenceErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsUpdateReconciliationEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsUpdateDiscoveryEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsUpdatePlatformServiceErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsUpdateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsUpdateArchivedReasonErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsUpdateTargetAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsUpdateActualAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsUpdateSloAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsUpdateSlaAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsUpdateK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsUpdateAddonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsUpdateVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsUpdateBlockNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsUpdateBlockConfigTemplateErrorComponent
            ):
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
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_actual_availability_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_addon_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateAddonErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_annotations_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_archived_at_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_archived_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_archived_reason_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_block_config_template_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateBlockConfigTemplateErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_block_name_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateBlockNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_criticality_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_debug_mode_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_discovery_enabled_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_display_name_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_k8s_cluster_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateK8SClusterErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_kind_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_labels_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_name_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_non_field_errors_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_order_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateOrderErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_platform_service_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_provider_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_provider_id_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_provider_reference_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_reconciliation_enabled_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_scope_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_sla_availability_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_sla_target_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_slo_availability_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_slo_target_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_target_availability_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_update_version_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsUpdateVersionErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesClusterAddonSubscriptionsUpdateActualAvailabilityErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsUpdateAddonErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsUpdateAnnotationsErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsUpdateArchivedAtErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsUpdateArchivedErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsUpdateArchivedReasonErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsUpdateBlockConfigTemplateErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsUpdateBlockNameErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsUpdateCriticalityErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsUpdateDebugModeErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsUpdateDiscoveryEnabledErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsUpdateDisplayNameErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsUpdateK8SClusterErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsUpdateKindErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsUpdateLabelsErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsUpdateNameErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsUpdateNonFieldErrorsErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsUpdateOrderErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsUpdatePlatformServiceErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsUpdateProviderErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsUpdateProviderIdErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsUpdateProviderReferenceErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsUpdateReconciliationEnabledErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsUpdateScopeErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsUpdateSlaAvailabilityErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsUpdateSlaTargetErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsUpdateSloAvailabilityErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsUpdateSloTargetErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsUpdateTargetAvailabilityErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsUpdateVersionErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_0 = (
                        ApiV1KubernetesClusterAddonSubscriptionsUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_1 = (
                        ApiV1KubernetesClusterAddonSubscriptionsUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_2 = (
                        ApiV1KubernetesClusterAddonSubscriptionsUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_3 = (
                        ApiV1KubernetesClusterAddonSubscriptionsUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_4 = (
                        ApiV1KubernetesClusterAddonSubscriptionsUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_5 = (
                        ApiV1KubernetesClusterAddonSubscriptionsUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_6 = (
                        ApiV1KubernetesClusterAddonSubscriptionsUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_7 = (
                        ApiV1KubernetesClusterAddonSubscriptionsUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_8 = (
                        ApiV1KubernetesClusterAddonSubscriptionsUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_9 = (
                        ApiV1KubernetesClusterAddonSubscriptionsUpdateReconciliationEnabledErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_10 = (
                        ApiV1KubernetesClusterAddonSubscriptionsUpdateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_11 = (
                        ApiV1KubernetesClusterAddonSubscriptionsUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_12 = (
                        ApiV1KubernetesClusterAddonSubscriptionsUpdateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_13 = (
                        ApiV1KubernetesClusterAddonSubscriptionsUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_14 = (
                        ApiV1KubernetesClusterAddonSubscriptionsUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_15 = (
                        ApiV1KubernetesClusterAddonSubscriptionsUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_16 = (
                        ApiV1KubernetesClusterAddonSubscriptionsUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_17 = (
                        ApiV1KubernetesClusterAddonSubscriptionsUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_18 = (
                        ApiV1KubernetesClusterAddonSubscriptionsUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_19 = (
                        ApiV1KubernetesClusterAddonSubscriptionsUpdateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_20 = (
                        ApiV1KubernetesClusterAddonSubscriptionsUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_21 = (
                        ApiV1KubernetesClusterAddonSubscriptionsUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_22 = (
                        ApiV1KubernetesClusterAddonSubscriptionsUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_23 = (
                        ApiV1KubernetesClusterAddonSubscriptionsUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_24 = (
                        ApiV1KubernetesClusterAddonSubscriptionsUpdateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_25 = (
                        ApiV1KubernetesClusterAddonSubscriptionsUpdateAddonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_26 = (
                        ApiV1KubernetesClusterAddonSubscriptionsUpdateVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_27 = (
                        ApiV1KubernetesClusterAddonSubscriptionsUpdateBlockNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_28 = (
                        ApiV1KubernetesClusterAddonSubscriptionsUpdateBlockConfigTemplateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_29 = (
                    ApiV1KubernetesClusterAddonSubscriptionsUpdateOrderErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_update_error_type_29

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_cluster_addon_subscriptions_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_cluster_addon_subscriptions_update_validation_error.additional_properties = d
        return api_v1_kubernetes_cluster_addon_subscriptions_update_validation_error

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
